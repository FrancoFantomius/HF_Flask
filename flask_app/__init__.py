from flask import Flask, render_template
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from os import path

def create_database(app):
    if not path.exists('website/' + db_name):
        database.create_all(app=app)
        print('Created Database!')

database = SQLAlchemy()
db_name = "HFaccounts.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
database.init_app(app)

#Blueprints
from flask_app.HF_accounts import HFauth
from flask_app.staticpages import pages
from flask_app.api import API

app.register_blueprint(HFauth, url_prefix="/accounts")
app.register_blueprint(pages, url_prefix="/")
app.register_blueprint(API, url_prefix="/api")

# Database
from .DB_Models import User, User_Computer

create_database(app)

# Login manager
login_manager = LoginManager()
login_manager.login_view = 'HFauth.signin'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(HFid):
    return User.query.get(str(HFid))

cors = CORS(app)

@app.errorhandler(404)
def pagenotfound(error):
    return render_template("PageNotFound.html"), 404# NEED TO MODIFY WITH A 404 PAGE


if __name__ == "__main__":
    app.run()