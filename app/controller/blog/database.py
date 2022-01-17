import os

import pymongo

from utils.config import DATABASE


class Database:

    def __init__(self):
        self.db = None

    def connect(self):
        if self.db is None:
            client = pymongo.MongoClient(os.environ.get("MONGO_CONNECTION_STRING"), tlsAllowInvalidCertificates=True)
            self.db = client[DATABASE]

    def get_entries(self):
        return list(self.db.entries.find())


db = Database()
