from fastapi import FastAPI
from meta_ai_api import MetaAI
import uvicorn

ai = MetaAI()
app = FastAPI()

@app.get("/ai")
async def get_ai_response(prompt: str):
    try:
        response = ai.prompt(message=prompt)
        return {"message": response["message"]}
    except Exception as err:
        return({
            "status": "Internal Server Error",
            "error": str(err),
        })

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)