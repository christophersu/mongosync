# Syncs a MongoDB collection with a list of dictionaries
# 
# Collection should be from PyMongo
# Key should be the field of the dictionaries to key by
def sync(collection, data, key):
    for doc in data:
        collection.find_and_modify(query={key: doc[key]},
            update={'$set': doc},
            upsert=True)

# Syncs a MongoDB collection with a JSON string
#
# Collection should be from PyMongo
# JSON data should be an array of dictionaries
# Key should be the field of the dictionaries to key by
def sync_json(collection, json_string, key):
    import json
    sync(collection, json.loads(json_string), key)