import secrets

from flask import Flask

from models.constants import HOSTNAME
from sites.blog.blog import app_blog
from sites.home.home import app_home


def create_app():
    app = Flask(__name__, host_matching=True, static_host=HOSTNAME)
    app.config['JSON_AS_ASCII'] = False
    app.config['CSRF_ENABLED'] = True
    app.secret_key = secrets.token_hex(24)

    app.register_blueprint(app_home)
    app.register_blueprint(app_blog)

    return app
