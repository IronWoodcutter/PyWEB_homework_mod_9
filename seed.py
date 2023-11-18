import json
from pymongo import MongoClient


myclient = MongoClient("mongodb+srv://Oleksandr:567234@goit.5380vln.mongodb.net/")

db = myclient["hw_web8"]
collection_authors = db["authors"]
collection_quotes = db["quotes"]


def upload_collection(file_name, Collection):
    with open(file_name, encoding='utf-8') as file:
        file_data = json.load(file)

    if isinstance(file_data, list):
        Collection.insert_many(file_data)
    else:
        Collection.insert_one(file_data)


if __name__ == '__main__':
    upload_collection('authors.json', collection_authors)
    upload_collection('quotes.json', collection_quotes)
