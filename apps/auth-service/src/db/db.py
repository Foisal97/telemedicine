from motor.motor_asyncio import AsyncIOMotorClient
from src.config.config import settings
client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.DB_NAME]

users_coll = db.get_collection("users")
sessions_coll = db.get_collection("sessions")

async def ensure_indexs():
    await users_coll.create_index("email", unique=True)
    await sessions_coll.create_index("email")
    await sessions_coll.create_index("expires_at")
    