import os

import pymongo
from flask import Blueprint, render_template, flash, request, session

from utils.config import HOSTNAME, DATABASE, PROTOCOL

site_blog = Blueprint("blog", __name__)


def get_url(site: str) -> str:
    url = f"{PROTOCOL}blog.{HOSTNAME}"
    if site != "index":
        url = f"{url}/{site}"
    return url


def render(site: str, **kwargs):
    return render_template(f"blog/{site}.html", url=get_url(site), **kwargs)


@site_blog.get("/", host=f"blog.{HOSTNAME}")
def index():
    client = pymongo.MongoClient(os.environ.get("MONGO_CONNECTION_STRING"), tlsAllowInvalidCertificates=True)
    db = client[DATABASE]
    entries = list(db.entries.find())
    username = None
    if "user" in session:
        username = session['user']
    print(username)
    return render(site="index", title="A small tech blog.", entries=entries)


def login(**kwargs):
    return render(site="login", title="Editor login.", **kwargs)


@site_blog.get("/login", host=f"blog.{HOSTNAME}")
def login_get():
    return login()


@site_blog.post("/login", host=f"blog.{HOSTNAME}")
def login_post():
    user = request.form.get('user')
    password = request.form.get('password')
    if f"{user}:{password}" == os.environ.get("BLOG_CREDENTIALS"):
        session['user'] = user
    else:
        flash('Sorry, the credentials are wrong.')
    return login()
