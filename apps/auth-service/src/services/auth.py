from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext

from src.config.config import settings
from src.repositories.user import UserRepository
from src.models.user import UserCreate

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
    
    