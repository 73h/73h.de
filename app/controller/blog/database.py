import os
from typing import Optional

import pymongo

from models.blog.article import Article
from models.blog.articles import Articles
from utils.config import DATABASE


class Database:

    def __init__(self):
        self.db = None

    def connect(self):
        if self.db is None:
            client = pymongo.MongoClient(os.environ.get("MONGO_CONNECTION_STRING"), tlsAllowInvalidCertificates=True)
            self.db = client[DATABASE]

    def get_articles(self) -> list:
        articles = list(self.db.entries.find())
        return Articles(articles).articles

    def get_article(self, url: str) -> Optional[Article]:
        articles = list(self.db.entries.find({"url": url}))
        if len(articles) == 1:
            return Article(**articles[0])
        return None


db = Database()
