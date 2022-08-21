from flask import Blueprint, request, redirect, url_for, flash, render_template
from flask_login import login_user, UserMixin, current_user, login_required, logout_user
import flask_app.database_API as db
import datetime
from datetime import date


HFauth = Blueprint("HFauth", __name__)

@HFauth.route("/signin", methods = ['GET', 'POST'])
def signin():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        log = db.login(email, password)
        if log == False or log == True:
            flash("The email or the password is wrong, please retry.", category="error")
        else:
            login_user(log, remember = True)
            return redirect(url_for("pages.index"))
    
    return render_template("signin.html", user = current_user)

@HFauth.route("/login")
def redir_signin():
    return redirect(url_for("HFauth.login"))

@HFauth.route("/signup", methods = ['GET', 'POST'])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        password_confirm = request.form.get("password_confirmation")
        name = request.form.get("name")
        birth = request.form.get("birth")

        #Checks values
        if len(email) > 250:
            flash("Email must be less than 250 characters", category="error")
        if len(password) < 7:
            flash("Password not enough long (min. 7 characters)", category="error")
        if password != password_confirm:
            flash("The password and the password confirmation are not the same", category="error")
        if len(name) > 250:
            flash("Name must be less than 250 characters", category="error")
        
        #is 13+ years old
        birth_year, birth_month, birth_day = birth.split("-")
        try:
            born = datetime.datetime(int(birth_year), int(birth_month), int(birth_day))
            today = date.today()
            if today.year - born.year - ((today.month, today.day) < (born.month, born.day)) < 13:
                flash("Users must be at least 13 years old", category="error")
        except ValueError:
            flash("Birthday given not valid", category="error")
        
        try:
            user = db.register(email, password, name, birth)
            login_user(user, remember = True)
            return redirect(url_for("pages.index"))
        except Exception:
            flash("Email already in use for another account", category="error")
    return render_template("signup.html", user=current_user)

@HFauth.route("/register")
def redir_signup():
    return redirect(url_for("HFauth.register"))

@HFauth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("pages.index"))
