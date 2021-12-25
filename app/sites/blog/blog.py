from flask import Blueprint, render_template

from models.constants import HOSTNAME

app_blog = Blueprint('blog', __name__)


@app_blog.get('/', host=f'blog.{HOSTNAME}')
def index():
    return render_template("blog/index.html")
