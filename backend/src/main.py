from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from src.service.rag import get_response


class ChatRequest(BaseModel):
    message: str

class ChatResponse():
    data: str 


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/chat")
async def root(chatRequest: ChatRequest):
    message = chatRequest.model_dump()
    chatResponse = get_response(message["message"])
    return {"chatResponse": chatResponse}
