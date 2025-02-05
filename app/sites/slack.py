import json

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
    if "token" in request.form and "text" in request.form:
        dump = json.dumps(request.form)
        response = {
            "response_type": "ephemeral",
            "text": f"Ich bin noch nicht fertig, aber ich arbeite dran! {dump}"
        }
        return response, 200
    return "", 200
