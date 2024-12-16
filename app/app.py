import secrets

from flask import Flask, redirect, url_for

from sites.blog.blog import site_blog
from sites.home.home import site_home
from sites.slack import site_slack
from sites.time_recording.time_recording import site_time_recording
from utils.config import HOSTNAME


def create_app():
    app = Flask(__name__, host_matching=True, static_host=HOSTNAME)
    app.config["JSON_AS_ASCII"] = False
    app.config["CSRF_ENABLED"] = True
    app.secret_key = secrets.token_hex(24)

    app.register_blueprint(site_home)
    app.register_blueprint(site_blog)
    app.register_blueprint(site_slack)
    app.register_blueprint(site_time_recording)

    host = f"{HOSTNAME}"

    @app.route('/<path:text>', host=f"blog.{host}")
    @app.route('/<path:text>', host=f"www.{host}")
    @app.route('/', host=f"blog.{host}")
    @app.route('/', host=f"www.{host}")
    def rd(text=""):
        rd_url = f"{url_for('blog.index')}{text}"
        return redirect(rd_url, code=301)

    return app
