
import os
import json
import boto3

REGION = os.environ.get("AWS_REGION_NAME", "ap-northeast-2")
AGENT_ID = os.environ["AGENT_ID"]
AGENT_ALIAS_ID = os.environ["AGENT_ALIAS_ID"]

bedrock_agent_runtime = boto3.client(
    "bedrock-agent-runtime",
    region_name=REGION
)

def handler(event, context):
    try:
        body = event.get("body", "{}")

        if event.get("isBase64Encoded"):
            import base64
            body = base64.b64decode(body).decode("utf-8")

        payload = json.loads(body)

        action = payload.get("action")
        if action not in ["opened", "reopened", "synchronize"]:
            return respond(200, {
                "message": f"ignored action: {action}"
            })

        repository = payload["repository"]["full_name"]
        owner, repo = repository.split("/")
        pr_number = payload["pull_request"]["number"]
        pr_url = payload["pull_request"]["html_url"]

        prompt = f"""
GitHub Pull Request를 자동 리뷰해주세요.

owner: {owner}
repo: {repo}
pr_number: {pr_number}
pr_url: {pr_url}

작업:
1. GitHub PR 정보를 조회하세요.
2. 변경된 코드의 스타일, 보안 취약점, 복잡도를 분석하세요.
3. 리뷰 결과를 GitHub PR 댓글로 등록하세요.
4. Slack으로 리뷰 완료 알림을 보내세요.
"""

        result_text = ""

        response = bedrock_agent_runtime.invoke_agent(
            agentId=AGENT_ID,
            agentAliasId=AGENT_ALIAS_ID,
            sessionId=f"github-pr-{owner}-{repo}-{pr_number}",
            inputText=prompt,
            enableTrace=False
        )

        for event_stream in response["completion"]:
            if "chunk" in event_stream:
                result_text += event_stream["chunk"]["bytes"].decode("utf-8")

        return respond(200, {
            "message": "review completed",
            "repository": repository,
            "pr_number": pr_number,
            "result": result_text
        })

    except Exception as e:
        return respond(500, {
            "error": str(e)
        })

def respond(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body, ensure_ascii=False)
    }
