from fastapi import FastAPI
from src.db import db

app = FastAPI()

@app.get("/")
async def check_connection():
    try:
        await db.command("ping")
        return {"message": "mongodb connection successfull"}
    except Exception as e:
        return {"error": str(e)}