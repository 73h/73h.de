import os
from typing import Optional

import pymongo
from bson import ObjectId

from models.blog.entries import Entries
from models.blog.entry import Entry
from utils.config import DATABASE


class Database:

    def __init__(self):
        self.db = None

    def connect(self):
        if self.db is None:
            client = pymongo.MongoClient(os.environ.get("MONGO_CONNECTION_STRING"), tlsAllowInvalidCertificates=True)
            self.db = client[DATABASE]

    def get_entries(self) -> list:
        entries = list(self.db.entries.find())
        return Entries(entries).entries

    def get_entry(self, _id: str) -> Optional[Entry]:
        entries = list(self.db.entries.find({"_id": ObjectId(_id)}))
        if len(entries) == 1:
            return Entry(**entries[0])
        return None


db = Database()
