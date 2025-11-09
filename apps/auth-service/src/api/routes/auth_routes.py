from fastapi import APIRouter, HTTPException, Request, Body
from pydantic import BaseModel

from src.middleware.rate_limiter import limiter
from src.models.user import UserCreate
from src.services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])

auth_service = AuthService()

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/signup")
async def signup(user: UserCreate):
    try:
        return await auth_service.signup(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
@limiter.limit("5/minute")
async def login(request: Request, payload: LoginRequest):
    try:
        return await auth_service.login(payload.email, payload.password, request=request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/refresh")
async def refresh_token(refresh_token: str = Body(..., embed=True)):
    try:
        return await auth_service.refresh_access_token(refresh_token)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    
    