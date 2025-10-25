from src.db.db import users_coll
from src.models.user import UserCreate
from bson import ObjectId, Binary, json_util

class UserRepository:
    async def create_user(self, user_data: dict):
        result = await users_coll.insert_one(user_data)
        return str(result.inserted_id)
    
    async def get_user_by_email(self, email:str):
        user = await users_coll.find_one({"email": email})
        return user
