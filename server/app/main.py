import secrets

from fastapi import FastAPI, Response, Request
from pydantic import BaseModel

app = FastAPI()

class Credentials(BaseModel):
  username: str
  password: str

@app.get("/")
async def home():
  return "Hello World"

@app.post("/login/")
async def login(data: Credentials, response: Response):
  token = secrets.token_urlsafe(32)
  response.set_cookie(
    httponly=True,
    key="secret_token",
    value=token,
    expires=10
  )
  return { "username": data.username, "secret_token": token }

@app.get("/token/")
async def check_token(request: Request):
  token = request.cookies.get("secret_token")
  return { "secret_token": token }
