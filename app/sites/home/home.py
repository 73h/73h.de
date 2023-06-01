from flask import Blueprint, render_template

from utils.config import HOSTNAME

site_home = Blueprint("home", __name__)
host = f"{HOSTNAME}"


@site_home.get("/ich", host=host)
def index():
    return render_template("home/index.html")
