from flask import Blueprint, flash, request, redirect, url_for, abort

from controller.blog.database import db
from controller.blog.login import user_login, user_logout
from controller.blog.render import render
from utils.config import HOSTNAME

site_blog = Blueprint("blog", __name__)


@site_blog.get("/", host=f"blog.{HOSTNAME}")
def index():
    db.connect()
    entries = db.get_entries()
    return render(site="index", title="A small tech blog.", entries=entries)


@site_blog.get("/entry/<_id>", host=f"blog.{HOSTNAME}")
def get_entry(_id: str):
    db.connect()
    entry = db.get_entry(_id)
    if entry is not None:
        return render(site="entry", title="A small tech blog.", entry=entry)
    abort(404)


@site_blog.get("/login", host=f"blog.{HOSTNAME}")
def login_get():
    return render(site="login", title="Editor login.")


@site_blog.post("/login", host=f"blog.{HOSTNAME}")
def login_post():
    if user_login(request.form.get('user'), request.form.get('password')):
        return redirect(url_for('blog.login_get'))
    flash('Sorry, das ist falsch.')
    return render(site="login", title="Editor login.")


@site_blog.get("/logout", host=f"blog.{HOSTNAME}")
def logout():
    user_logout()
    return redirect(url_for('blog.index'))


@site_blog.get("/impressum", host=f"blog.{HOSTNAME}")
def impressum():
    return render(site="impressum", title="Impressum.")


@site_blog.get("/datenschutz", host=f"blog.{HOSTNAME}")
def datenschutz():
    return render(site="datenschutz", title="Datenschutz.")
