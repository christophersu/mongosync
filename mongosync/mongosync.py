# Syncs a MongoDB collection with a list of dictionaries

# Collection should be from PyMongo
# Key should be the field of the dictionaries to key by
def sync(collection, data, key):
    for doc in data:
        collection.find_and_modify(query={key: doc[key]},
            update={'$set': doc},
            upsert=True)