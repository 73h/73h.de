from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    app.config['CSRF_ENABLED'] = True

    @app.get('/')
    def index():
        return render_template("index.html")

    return app
