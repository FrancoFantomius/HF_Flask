from flask import Blueprint, request, redirect, url_for, flash, render_template
from flask_login import login_user, UserMixin, current_user, login_required, logout_user
import flask_app.database_API as db


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
            login_user(log, remember = True)
            return redirect(url_for("pages.index"))
    
    return render_template("login.html", user = current_user)

@HFauth.route("/login")
def redir_signin():
    return redirect(url_for("HFauth.login"))

@HFauth.route("/signup", methods = ['GET', 'POST'])
def register():#                                        To be modified
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        name = request.form.get("name")
        birth = request.form.get("birth")

        #Values verification
        if len(email) > 250:
            flash("Email must be less than 250 characters", category="error")
        if len(password) < 7:
            flash("Password not enough long (min. 7 characters)", category="error")
        if len(name) > 250:
            flash("Name must be less than 250 characters", category="error")
        
        user = db.register(email, password, name, birth)
        login_user(user, remember = True)

        return redirect(url_for("pages.index"))
    return render_template("register.html", user=current_user)

@HFauth.route("/register")
def redir_signup():
    return redirect(url_for("HFauth.register"))

@HFauth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("pages.index"))
