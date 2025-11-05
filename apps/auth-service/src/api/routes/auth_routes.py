from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
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
async def login(payload: LoginRequest):
    try:
        return await auth_service.login(payload.email, payload.password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    
    