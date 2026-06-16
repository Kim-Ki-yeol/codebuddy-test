# CodeBuddy

Amazon Bedrock Agent 기반 AI 코드 리뷰 자동화 시스템

## 프로젝트 개요

CodeBuddy는 GitHub Pull Request 생성 시 Amazon Bedrock Agent를 활용하여 자동으로 코드 리뷰를 수행하고, GitHub 댓글 및 Slack 알림을 생성하는 AI 기반 코드 리뷰 자동화 시스템입니다.

GitHub Webhook을 통해 Pull Request 이벤트를 감지하고, AWS API Gateway와 Lambda를 통해 Bedrock Agent를 호출하여 코드 스타일, 보안 취약점, 코드 복잡도를 분석합니다.

---

## Architecture

```text
GitHub Pull Request
        ↓
 GitHub Webhook
        ↓
    API Gateway
        ↓
      Lambda
        ↓
 Amazon Bedrock Agent
        ↓
 ┌───────────────┬───────────────┐
 ↓               ↓
GitHub Comment   Slack Notification
```

---

## 주요 기능

### GitHub Pull Request 자동 감지

* GitHub Webhook 기반 PR 이벤트 수신
* Open / Reopen / Synchronize 이벤트 처리

### AI 코드 리뷰

* PEP8 기반 코드 스타일 검사
* OWASP 기반 보안 취약점 검사
* 코드 복잡도 분석
* 리뷰 결과 자동 생성

### 자동 알림

* GitHub PR 댓글 자동 등록
* Slack 채널 자동 알림 전송

### CloudFormation 기반 배포

* API Gateway 자동 생성
* Lambda 자동 생성
* IAM Role 자동 생성
* 원클릭 배포 지원

---

## 기술 스택

### AWS

* Amazon Bedrock
* Bedrock Agent
* Knowledge Base
* AWS Lambda
* API Gateway
* CloudFormation
* IAM

### DevOps

* GitHub Webhook
* GitHub API
* Slack API

### AI

* Claude 3 Sonnet
* Retrieval Augmented Generation (RAG)

---

## 프로젝트 구조

```text
codebuddy-agent/
├── README.md
├── cloudformation/
│   └── template.yaml
├── lambda/
│   └── orchestrator.py
├── docs/
│   └── api-spec.yaml
├── demo/
│   └── demo.mp4
└── CodeBuddy_Agent_과제.ipynb
```

---

## 배포 방법

### 사전 준비

* GitHub Personal Access Token 생성
* Slack Incoming Webhook 생성
* Amazon Bedrock Agent 생성
* Agent Alias 생성

### CloudFormation 배포

```bash
aws cloudformation deploy \
  --template-file cloudformation/template.yaml \
  --stack-name CodeBuddyStack \
  --capabilities CAPABILITY_NAMED_IAM \
  --region ap-northeast-2 \
  --parameter-overrides \
  AgentId=<AGENT_ID> \
  AgentAliasId=<AGENT_ALIAS_ID> \
  GitHubToken=<GITHUB_TOKEN> \
  SlackWebhookUrl=<SLACK_WEBHOOK_URL>
```

배포 완료 후 생성된 Webhook URL을 GitHub Repository Webhook에 등록합니다.

---

## 사용 방법

1. GitHub Repository에 Pull Request 생성
2. GitHub Webhook 이벤트 발생
3. Lambda가 Bedrock Agent 호출
4. AI 코드 리뷰 수행
5. GitHub 댓글 등록
6. Slack 알림 전송

---

## 시연 결과

### GitHub PR 자동 리뷰

* Pull Request 생성 시 자동 리뷰 수행
* GitHub 댓글 자동 등록

### Slack 알림

* 리뷰 완료 알림 자동 전송
* PR 링크 및 분석 결과 제공

---

## 구현 결과

### 자동화 흐름

```text
PR 생성
→ GitHub Webhook
→ API Gateway
→ Lambda
→ Bedrock Agent
→ GitHub 댓글
→ Slack 알림
```

### 테스트 결과

* GitHub PR 자동 감지 성공
* GitHub 댓글 자동 등록 성공
* Slack 알림 자동 전송 성공
* End-to-End 자동화 검증 완료

---

## 회고

* Amazon Bedrock Agent와 Tool Use 활용 경험
* Knowledge Base 기반 RAG 구현 경험
* GitHub Webhook 기반 이벤트 자동화 경험
* AI 기반 코드 리뷰 자동화 시스템 구축 경험
* CloudFormation을 활용한 인프라 자동 배포 경험
