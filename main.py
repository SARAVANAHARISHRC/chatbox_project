# main.py
from fastapi import FastAPI
from pydantic import BaseModel

from chat_logic import get_response

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post("/chat")
def chat_endpoint(msg: Message):
    user_input = msg.message
    response = get_response(user_input)
    return {"response": response}

@app.get("/")
def root():
    return {"message": "Chatbot backend is running"}
