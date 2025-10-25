from fastapi import APIRouter, HTTPException
from src.models.user import UserCreate
from src.services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])

auth_service = AuthService()

@router.post("/signup")
async def signup(user: UserCreate):
    try:
        return await auth_service.signup(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    