from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes.auth_routes import router as auth_router
from src.config.config import settings
from src.db.db import ensure_indexs

app = FastAPI(
    title= "Telemedicine Auth Service",
    version="1.0.0",
    description="Handles user signup, login and JWT authentication"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router)

@app.on_event("startup")
async def startup_event():
    await ensure_indexs()


@app.get("/")
async def root():
    return {"message": "Auth Service is running", "status": "ok"}
