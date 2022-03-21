import os
from dotenv import load_dotenv
from os.path import join, dirname
from pymongo import MongoClient


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Database:
    URI = os.environ.get("URI")
    client = MongoClient(URI)
    db = client.habit_tracker

    def __init__(self):
        pass

    @classmethod
    def insert_to_db(cls, collection, content):
        cls.db[collection].insert_one(content)

    @classmethod
    def find_from_db(cls, collection, query):
        return [item for item in cls.db[collection].find(query)]

    @classmethod
    def update_record(cls, collection, _id, data):
        cls.db[collection].update_one({'_id': _id}, {'$set': data}, upsert=False)
