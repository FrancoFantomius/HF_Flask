from flask import Blueprint, request, redirect, url_for

API = Blueprint("API", __name__)

@API.route("/docs")
def docs():
    return "WIP"