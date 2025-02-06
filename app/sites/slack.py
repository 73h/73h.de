import json
import os
import datetime
from math import floor

import requests
from flask import Blueprint, request

from utils.config import HOSTNAME, POKER_API

site_slack = Blueprint("slack", __name__)
host = f"{HOSTNAME}"


@site_slack.post("/slack", host=host)
def index():
    if "token" in request.form and "text" in request.form:
        result = requests.post(POKER_API, data=request.form)
        return result.json(), result.status_code
    return "", 200

@site_slack.post("/wie-lange-noch", host=host)
def wie_lange_noch():
    return rente("Stephan", 2025, 12, 31)

@site_slack.post("/rente/<name>/<y>/<m>/<d>", host=host)
def rente(name, y, m, d):
    end_date = datetime.datetime(int(y), int(m), int(d), 17, 0, 0)
    delta = end_date - datetime.datetime.now()
    days = delta.days
    hours = floor(delta.seconds/60/60)
    minutes = floor(delta.seconds/60)-hours*60
    seconds = delta.seconds-(minutes*60+hours*60*60)
    response = {
        "response_type": "ephemeral",
        "text": f"{name} arbeitet noch {days} Tage, {hours} Stunden, {minutes} Minuten und {seconds} Sekunden für uns."
    }
    return response, 200
