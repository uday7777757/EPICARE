from pymongo import MongoClient

def get_db():
    uri = "mongodb+srv://udaysuri2020:Uday2020@cluster0.wmiqd.mongodb.net/"
    client = MongoClient(uri)
    db = client["medid"]  # Your database name
    return db
