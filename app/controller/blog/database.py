import os
from datetime import datetime
from typing import Optional

import pymongo

from models.blog.article import Article
from models.blog.articles import Articles
from models.time_recording.time_recording import TimeRecording
from models.time_recording.time_recordings import TimeRecordings
from utils.config import DATABASE


class Database:

    def __init__(self):
        self.db = None

    def connect(self):
        if self.db is None:
            client = pymongo.MongoClient(os.environ.get("MONGO_CONNECTION_STRING"), tlsAllowInvalidCertificates=True)
            self.db = client[DATABASE]

    def get_articles(self, with_unpublished=False) -> list:
        conditions = {}
        if not with_unpublished:
            conditions["published"] = True
        articles = list(self.db.articles.find(conditions).sort("created", -1))
        return Articles(articles).articles

    def get_article(self, url: str) -> Optional[Article]:
        articles = list(self.db.articles.find({"url": url}))
        if len(articles) == 1:
            return Article(**articles[0])
        return None

    def title_exists(self, article: Article) -> bool:
        articles = list(self.db.articles.find({"url": article.url}))
        return len(articles) == 1 and articles[0]["_id"] != article.id

    def update_article(self, article: Article) -> bool:
        if not self.title_exists(article):
            self.db.articles.update_one({'_id': article.id}, {"$set": article.get_save_object()}, upsert=False)
            return True
        return False

    def insert_article(self, article: Article) -> bool:
        if not self.title_exists(article):
            self.db.articles.insert_one(article.get_save_object())
            return True
        return False

    def delete_article(self, article: Article):
        self.db.articles.delete_one({'_id': article.id})

    def get_time_recordings(self, user: str, year: int) -> list:
        start = datetime(year, 1, 1, 0, 0, 0)
        end = datetime(year, 12, 31, 23, 59, 59)
        time_recordings = list(self.db.time_recording.find({
            "user": user,
            "date": {'$lt': end, '$gte': start}
        }))
        return TimeRecordings(time_recordings).time_recordings


db = Database()
