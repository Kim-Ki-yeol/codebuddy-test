def get_user(id):
    query = f"SELECT * FROM users WHERE id = {id}"
    return db.execute(query)

def Sum(a,b):
  return a+b
