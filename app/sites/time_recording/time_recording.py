from datetime import datetime, timedelta

from flask import Blueprint, render_template, url_for, redirect

from controller.blog.database import db
from models.time_recording.time_recording import TimeRecording
from utils.config import HOSTNAME

site_time_recording = Blueprint("time_recording", __name__)
host = f"{HOSTNAME}"

@site_time_recording.get("/time-recording", host=host)
def index():
    #TODO: Implement create new user
    return "Create new user"

@site_time_recording.get("/time-recording/<user>", host=host)
def index_user(user: str):
    rd_url = f"{url_for('time_recording.index_user_year', user=user, year=2025)}"
    return redirect(rd_url, code=302)

def get_calender(year: int) -> list[TimeRecording]:
    calender = []
    start = datetime(year, 1, 1)
    while start.year == year:
        calender.append(TimeRecording(date=start))
        start = start + timedelta(days=1)
    return calender

@site_time_recording.get("/time-recording/<user>/<year>", host=host)
def index_user_year(user: str, year: str):
    try:
        year = int(year)
    except ValueError:
        return "Year must be an integer"
    db.connect()
    time_recordings = db.get_time_recordings(user, year)
    calender = get_calender(year)
    ui_calender = []
    for day in calender:
        for time_recording in time_recordings:
            ui_calender.append(time_recording) if day.date == time_recording.date else ui_calender.append(day)
    return render_template("time_recording/index.html", calender=ui_calender)
