from datetime import datetime
from passlib.context import CryptContext
from src.db.db import sessions_coll

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

class SessionRepository:
    async def create_session(self, email:str, refresh_token:str, expires_at:datetime, ip_address:str, device_name:str):
        hashed_token = pwd_context.hash(refresh_token)
        await sessions_coll.insert_one({
            "email": email,
            "token_hash": hashed_token,
            "expires_at": expires_at,
            "created_at": datetime.utcnow(),
            "ip_address": ip_address,
            "device_name": device_name
        })

    async def verify_session(self, email:str, refresh_token:str) -> bool:
        session = await sessions_coll.find_one({"email":email})
        if not session:
            return False
        return pwd_context.verify(refresh_token, session["token_hash"])
    
    async def delete_session(self, email:str):
        await sessions_coll.delete_many({"email": email})
