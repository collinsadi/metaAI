from fastapi import FastAPI
from meta_ai_api import MetaAI

ai = MetaAI()
app = FastAPI()

@app.get("/ai")
async def get_ai_response(prompt: str):
    response = ai.prompt(message=prompt)
    return {"message": response["message"]}