from fastapi import Request
from user_agents import parse
from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext

from src.config.config import settings
from src.repositories.user import UserRepository
from src.repositories.seesions import SessionRepository
from src.models.user import UserCreate
from src.utils.token import create_access_token, create_refresh_token, verify_refresh_token

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

class AuthService:
    def __init__(self):
        self.repo = UserRepository ()
        self.session_repo = SessionRepository()


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
    

    async def login(self, email: str, password: str, request: Request):
        user = await self.repo.get_user_by_email(email)
        if not user or not self.verify_password(password, user["hased_password"]):
            raise ValueError("Invalid Credentials")
        
        access_token = create_access_token(data={"sub": user["email"]}, expire_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
        
        refresh_expire = timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        refresh_token = create_refresh_token(data={"sub": user["email"]}, expire_delta=refresh_expire)

        expires_at = datetime.utcnow() + refresh_expire
        ip_address = request.headers.get("X-Forwarded-For")
        if ip_address:
            ip_address = ip_address.split(",")[0].strip()
            print(f"IP Address from X-Forwarded-For: {ip_address}")
        else:
            ip_address = request.client.host    
        user_agent = parse(request.headers.get("User-Agent", ""))
        device_name = f"{user_agent.browser.family} on {user_agent.os.family}"
 
        await self.session_repo.create_session(
            email=user["email"],
            refresh_token=refresh_token,
            expires_at=expires_at,
            ip_address=ip_address,
            device_name=device_name
        )
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }
    

    async def refresh_access_token(self, refresh_token: str):
        email = verify_refresh_token(refresh_token)
        if not email:
            raise ValueError("Invalid Refresh Token")
        
        session = await self.session_repo.get_session_by_token(refresh_token)
        print("session retrieved for refresh:", session)
        if not session:
            raise ValueError("Session Not Found")
        
        new_access_token = create_access_token(data={"sub": email}, expire_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
        return {
            "access_token": new_access_token,
            "token_type": "bearer"
        }

    
    