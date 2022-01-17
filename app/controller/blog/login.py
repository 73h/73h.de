import os

from flask import session


def is_user_logged_in() -> bool:
    return "user" in session and os.environ.get("BLOG_CREDENTIALS").startswith(session.get("user"))


def get_logged_in_user() -> str:
    if is_user_logged_in():
        return session.get("user")
    return ""


def user_login(user: str, password: str) -> bool:
    if f"{user}:{password}" == os.environ.get("BLOG_CREDENTIALS"):
        session['user'] = user
        return True
    return False


def user_logout():
    if is_user_logged_in():
        session.pop("user")
