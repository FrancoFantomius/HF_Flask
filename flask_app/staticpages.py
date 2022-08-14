from flask import Blueprint, redirect, url_for, render_template
from flask_login import login_required

pages = Blueprint("pages", __name__)

@pages.route("/")
def index():
    return render_template("index.html")


@pages.errorhandler(404)
def pagenotfound(error):
    return render_template("index.html"), 404# NEED TO MODIFY WITH A 404 PAGE
