import mongosync
from pymongo import MongoClient

test_data = [
    {
        'test': 'hello',
        'key': 1
    },
    {
        'another': 'thing',
        'key': 2
    }
]

other_data = [
    {
        'test': 'different!',
        'key': 1
    },
    {
        'another': 'thing',
        'key': 2
    }
]

client = MongoClient()
db = client.test_database
collection = db.test_collection

mongosync.sync(collection, other_data, 'key')