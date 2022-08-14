from flask import Flask, render_template, request, redirect
from flask_app import app
import flask_app.database as db

#Blueprints
from flask_app.HF_accounts import HFauth
from flask_app.staticpages import pages


app.register_blueprint(HFauth, url_prefix="/accounts")
app.register_blueprint(pages, url_prefix="/")


@app.errorhandler(404)
def pnf(error):
    return render_template("404.html"), 404

if __name__=="__main__":
    app.run()#debug=True)