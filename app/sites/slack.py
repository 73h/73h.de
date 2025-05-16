import json
import os
import datetime
import re
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

def letters_to_int(typ, length, letters = "") -> str:
    result = ""
    if typ == "linear":
        result = 0
    letters = letters.upper().replace("Ä", "AE").replace("Ü", "UE").replace("Ö", "OE").replace("ß", "ss")
    letters = re.sub(r"[^A-Z]", "", letters)
    letters = letters.ljust(int(length),"A")[:int(length)]
    i = int(length)-1
    for c in letters:
        if typ == "linear":
            result += (ord(c) - 65) * 26**i
        else:
            result += str(ord(c) - 55)
        i += -1
    if typ == "linear":
        result += 1
    return str(result)

@site_slack.post("/letters-to-int/<typ>/<length>", host=host)
def letters_to_int_route_with_typ(typ, length):
    message = "Gib mir bitte ein paar Buchstaben - ich mag Buchstaben! :smiley:"
    if request and "text" in request.form:
        letters = request.form["text"].split(" ")
        result = []
        for l in letters:
            if l:
                result.append(letters_to_int(typ, length, l))
        if len(result) > 0:
            message = " | ".join(result)
    response = {
        "response_type": "ephemeral",
        "text": f"{str(message)}"
    }
    return response, 200

@site_slack.post("/letters-to-int/<length>", host=host)
def letters_to_int_route(length):
    return letters_to_int_route_with_typ("blockwise", length)

if __name__ == "__main__":
    print(letters_to_int("blockwise", 4, "a"))
    print(letters_to_int("blockwise", 4, "z"))
    print(letters_to_int("linear", 4, "a"))
    print(letters_to_int("linear", 4, "z"))
