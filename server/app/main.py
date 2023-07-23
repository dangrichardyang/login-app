import secrets
import redis
import json

from datetime import datetime, timezone, timedelta
from fastapi import FastAPI, Response, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
db = redis.Redis(host="redis")

origins = [
#    "http://localhost",
#    "http://localhost:3000",
    "http://10.0.0.31",
    "http://10.0.0.31:3000",
#    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Credentials(BaseModel):
  username: str
  password: str

@app.get("/")
async def home():
  return "Hello World 2"

@app.post("/login")
async def login(data: Credentials, response: Response):
  error = HTTPException(status_code=401, detail="Incorrect username and/ or password")

  if not data.username or not data.password: raise error

  user = data.username.lower()
  if user != "user" or data.password != "pass": raise error

  token = secrets.token_urlsafe(32)
  expires = datetime.now(timezone.utc) + timedelta(seconds=10)
  user_info = json.dumps({"user": user, "roles": ["user"]})
  db.set(name=token, value=user_info, exat=expires)
  response.set_cookie(
    httponly=True,
    key="secret_token",
    value=token,
    expires=expires
  )
  return { "detail": "You have successfully logged in"}

@app.get("/user")
async def get_user_info(request: Request):
  error = HTTPException(status_code=403, detail="You are not authooized")
  token = request.cookies.get("secret_token")
  if not token: raise error

  data = db.get(name=token)
  if not data: raise error

  user_info = json.loads(data)
  return { "user_info": user_info }

@app.get("/logout")
async def logout(request: Request, response: Response):
  token = request.cookies.get("secret_token")
  if token: db.delete(token)
  response.delete_cookie(key="secret_token")
  return { "detail": "You have been successfully logged out"}
