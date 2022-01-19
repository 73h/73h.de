from flask import render_template

from controller.blog.login import is_user_logged_in, get_logged_in_user
from utils.http import Http


def get_url(site: str = "") -> str:
    http = Http()
    url = http.url
    if site != "index":
        url = f"{http.url}/{site}"
    return url


def render(site: str, **kwargs):
    logged_in = is_user_logged_in()
    user = get_logged_in_user().capitalize()
    return render_template(f"blog/{site}.html", url=get_url(site), logged_in=logged_in, user=user, **kwargs)
