from flask import Blueprint, render_template

from utils.config import HOSTNAME

site_home = Blueprint("home", __name__)


@site_home.get("/", host=HOSTNAME)
@site_home.get("/", host=f"www.{HOSTNAME}")
def index():
    return render_template("home/index.html")
