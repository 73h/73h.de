import secrets

from flask import Flask, request, redirect

from models.constants import HOSTNAME
from sites.blog.blog import site_blog
from sites.home.home import site_home


def create_app():
    app = Flask(__name__, host_matching=True, static_host=HOSTNAME)
    app.config['JSON_AS_ASCII'] = False
    app.config['CSRF_ENABLED'] = True
    app.secret_key = secrets.token_hex(24)

    @app.before_request
    def before_request():
        if not request.is_secure:
            url = request.url.replace('http://', 'https://', 1)
            return redirect(url, code=301)

    app.register_blueprint(site_home)
    app.register_blueprint(site_blog)

    return app
