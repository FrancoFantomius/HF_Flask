from flask import Blueprint, request, redirect, url_for, flash, render_template
from flask_login import login_user, UserMixin, current_user, login_required, logout_user
import flask_app.database as db


class User(UserMixin):
    def __init__(self, HFid, email, birth, name):
        self.HFid = HFid
        self.email = email
        self.name = name
        self.birth = birth

HFauth = Blueprint("HFauth", __name__)

@HFauth.route("/signin", methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        log = db.login(email, password)
        if log == False or log == True:
            flash("The email or the password is wrong, please retry.", category="error")
        else:
            log_info = db.get_info(log)
            user = User(log, email, log_info[3], log_info[2])
            login_user(user, remember = True)
            return redirect(url_for("pages.index"))
    return render_template("login.html", user = current_user)

@HFauth.route("/login")
def redir_signin():
    return redirect(url_for("login"))

@HFauth.route("/signup", methods = ['GET', 'POST'])
def register():#                                        To be modified
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        name = request.form.get("name")
        birth = request.form.get("birth")
        HFid = db.register(email, password, name, birth)
        user = User(HFid, email, birth, name)
        login_user(user, remember = True)
        return redirect(url_for("pages.index"))
    return render_template("register.html", user=current_user)

@HFauth.route("/register")
def redir_signup():
    return redirect(url_for("register"))

@HFauth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("pages.index"))
