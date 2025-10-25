from motor.motor_asyncio import AsyncIOMotorClient
from src.config.config import settings
client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.DB_NAME]

users_coll = db.get_collection("users")

async def ensure_indexs():
    await users_coll.create_index("email", unique=True)