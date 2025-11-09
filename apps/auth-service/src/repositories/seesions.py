from datetime import datetime
from passlib.context import CryptContext
from src.db.db import sessions_coll

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

class SessionRepository:
    async def create_session(self, email:str, refresh_token:str, expires_at:datetime, ip_address:str, device_name:str):
        await sessions_coll.insert_one({
            "email": email,
            "refresh_token": refresh_token,
            "expires_at": expires_at,
            "created_at": datetime.utcnow(),
            "ip_address": ip_address,
            "device_name": device_name
        })

    async def verify_session(self, email:str, refresh_token:str) -> bool:
        session = await sessions_coll.find_one({"email":email})
        print("session found:", session)
        if not session:
            return False
        a = pwd_context.verify(refresh_token, session["token_hash"])
        print("password verify result:", a)
        return a
    
    async def get_session_by_token(self, refresh_token:str):
        session = await sessions_coll.find_one({"refresh_token": refresh_token})
        return session
    
    
    async def delete_session(self, email:str):
        await sessions_coll.delete_many({"email": email})
