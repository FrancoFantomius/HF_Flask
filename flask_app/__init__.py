from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from os import path

database = SQLAlchemy()
db_name = "HF.db"

def new_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "5fc06346b4c608e9defd8f097313094e8d49ea3a0c74da535f64850cfacf4fd0"
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

    return app





def create_database(app):
    if not path.exists('website/' + db_name):
        database.create_all(app=app)
        print('Created Database!')