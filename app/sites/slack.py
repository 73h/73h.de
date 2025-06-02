import json
import os
import datetime
import re
import unicodedata
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

def letters_to_int(calculation_length, letters = "") -> str:
    # We start with 1 so that A = 1
    result = 1
    # Normalise the string to remove accents and diacritics
    # For example, "kožušček" becomes "kozuscek" or "café" becomes "cafe"
    letters = "".join(c for c in unicodedata.normalize('NFD', letters) if unicodedata.category(c) != 'Mn')
    # Convert to upper case, replace ß with ss and remove all other non-alphabetic characters
    letters = letters.upper()
    letters = letters.replace("ß", "ss")
    letters = re.sub(r"[^A-Z]", "", letters)
    # Fill the character string with “A” on the right-hand side if it is shorter than the calculation length and shorten it to the calculation length
    letters = letters.ljust(int(calculation_length),"A")[:int(calculation_length)]
    i = int(calculation_length)-1
    for c in letters:
        # Calculate the value of each letter A=AA=AAA=AAAA=1, AAAB=2, ..., AAAZ=26, ..., ZZZZ=456976 when calculation_length=4
        result += (ord(c) - 65) * 26**i
        i += -1
    return str(result)

@site_slack.post("/letters-to-int/<length>", host=host)
def letters_to_int_route(length):
    message = "Gib mir bitte ein paar Buchstaben - ich mag Buchstaben! :smiley:"
    if request and "text" in request.form:
        letters = request.form["text"].split(" ")
        result = []
        for l in letters:
            if l:
                result.append(letters_to_int(length, l))
        if len(result) > 0:
            message = " | ".join(result)
    response = {
        "response_type": "ephemeral",
        "text": f"{str(message)}"
    }
    return response, 200

if __name__ == "__main__":
    print(letters_to_int(4, "a"))
    print(letters_to_int(4, "zzzz"))
