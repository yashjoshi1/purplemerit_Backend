from pymongo import MongoClient
from app.config import settings

client = MongoClient(settings.MONGO_URI)
db = client[settings.DATABASE_NAME]

users_collection = db.users
print("MONGO_URI:", settings.MONGO_URI)
print("DB NAME:", settings.DATABASE_NAME)
