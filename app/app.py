import secrets

from flask import Flask

from sites.blog.blog import site_blog
from sites.home.home import site_home
from utils.config import HOSTNAME


def create_app():
    app = Flask(__name__, host_matching=True, static_host=HOSTNAME)
    app.config["JSON_AS_ASCII"] = False
    app.config["CSRF_ENABLED"] = True
    app.secret_key = secrets.token_hex(24)

    app.register_blueprint(site_home)
    app.register_blueprint(site_blog)

    return app
