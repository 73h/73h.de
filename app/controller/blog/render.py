from flask import render_template

from controller.blog.login import is_user_logged_in, get_logged_in_user
from utils.http import Http


def get_url(site: str = "", **kwargs) -> str:
    http = Http()
    url = http.url
    if site != "index":
        url = url + f"/{site}"
    if "article" in kwargs:
        article_url = kwargs["article"].url
        url = url + f"/{article_url}"
    return url


def render(site: str, **kwargs):
    logged_in = is_user_logged_in()
    user = get_logged_in_user().capitalize()
    return render_template(f"blog/{site}.html", asset_version="?v1", url=get_url(site, **kwargs), logged_in=logged_in,
                           user=user, **kwargs)
