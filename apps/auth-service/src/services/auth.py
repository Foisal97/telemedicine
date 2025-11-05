from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext

from src.config.config import settings
from src.repositories.user import UserRepository
from src.models.user import UserCreate
from src.utils.token import create_access_token, create_refresh_token, verify_refresh_token

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

class AuthService:
    def __init__(self):
        self.repo = UserRepository ()

    def hashed_password(self, password: str) -> str:
        password = password[:72]
        return pwd_context.hash(password)
    
    def verify_password(self, plain_password, hashed_password) -> bool:
        return pwd_context.verify(plain_password, hashed_password)
    
    async def signup(self, user: UserCreate):
        existing_user = await self.repo.get_user_by_email(user.email)
        if existing_user:
            raise ValueError("User Already Exists")
        
        hashed_pw = self.hashed_password(user.password)
        user_data = {
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "hased_password": hashed_pw
        }

        user_id = await self.repo.create_user(user_data)
        return {"id": user_id, "email": user.email}
    
    async def login(self, email: str, password: str):
        user = await self.repo.get_user_by_email(email)
        if not user or not self.verify_password(password, user["hased_password"]):
            raise ValueError("Invalid Credentials")
        access_token = create_access_token(data={"sub": user["email"]}, expire_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
        refresh_token = create_refresh_token(data={"sub": user["email"]}, expire_delta=timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS))

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }
    
    async def refresh_access_token(self, refresh_token: str):
        try:
            email = verify_refresh_token(refresh_token)
            new_access_token = create_access_token(data={"sub": email})
            return {
                "access_token": new_access_token,
                "token_type": "bearer"
            }
        except ValueError:
            raise ValueError("Invalid Refresh Token")
    