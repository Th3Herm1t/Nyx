# utils.py
import pymongo
from django.conf import settings

def get_mongo_connection():
    client = pymongo.MongoClient(settings.MONGODB_URL)
    return client
