from flask import Blueprint, redirect, url_for, render_template
from flask_login import login_required

pages = Blueprint("pages", __name__)

@pages.route("/")
def index():
    return render_template("index.html")

@pages.route("/apps")
def app_show():
    return "WIP"

@pages.route("/contact")
def contact_us():
    return "WIP"
