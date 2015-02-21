import mongosync
from pymongo import MongoClient

test_json = '[{"key": 1, "hello": "different"}]'

client = MongoClient()
db = client.test_database
collection = db.test_collection

mongosync.sync_json(collection, test_json, 'key')