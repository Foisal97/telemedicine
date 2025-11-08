from fastapi import FastAPI
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded

from src.middleware.cors import add_cors_middleware
from src.middleware.rate_limiter import limiter
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes.auth_routes import router as auth_router
from src.config.config import settings
from src.db.db import ensure_indexs

app = FastAPI(
    title= "Telemedicine Auth Service",
    version="1.0.0",
    description="Handles user signup, login and JWT authentication"
)


app.state.limiter = limiter
add_cors_middleware(app)

app.include_router(auth_router)

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request, exc):
    return JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded. Try again later."}
    )

@app.on_event("startup")
async def startup_event():
    await ensure_indexs()


@app.get("/")
async def root():
    return {"message": "Auth Service is running", "status": "ok"}
