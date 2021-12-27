import os

import pymongo
from flask import Blueprint, render_template

from models.constants import HOSTNAME

site_blog = Blueprint("blog", __name__)


@site_blog.get("/", host=f"blog.{HOSTNAME}")
def index():
    client = pymongo.MongoClient(
        os.environ.get("MONGO_CONNECTION_STRING"),
        tlsAllowInvalidCertificates=True)
    db = client.blog
    entries = list(db.entries.find())
    return render_template("blog/index.html", entries=entries)
