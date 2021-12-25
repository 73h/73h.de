from flask import Blueprint, render_template

from models.constants import HOSTNAME

app_home = Blueprint('home', __name__)


@app_home.get('/', host=HOSTNAME)
@app_home.get('/', host=f'www.{HOSTNAME}')
def index():
    return render_template("home/index.html")
