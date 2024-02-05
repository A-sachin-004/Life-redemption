from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    message: str

messages = []

@app.get("/messages")
async def read_messages():
    print(messages)
    return messages

@app.post("/messages")
async def send_message(message: Message):
    if not message.message:
        raise HTTPException(status_code=422, detail="Message cannot be empty")
    print(message.message)
    messages.append(message.message)
    return {"message": "Message sent successfully"}
