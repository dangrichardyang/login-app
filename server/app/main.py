from typing import Annotated

from fastapi import FastAPI, Form

app = FastAPI()

@app.get("/")
async def home():
  return "Hello World"

@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}
