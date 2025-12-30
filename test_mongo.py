from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://purplemerit_user:Password@purplemerit.o2yudml.mongodb.net"
)

print(client.list_database_names())
