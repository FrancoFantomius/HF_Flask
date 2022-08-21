from . import database
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(database.Model, UserMixin):
    HFid = database.Column(database.String(50), primary_key=True)
    name = database.Column(database.String(250))
    email = database.Column(database.String(250), unique = True)
    password_hash = database.Column(database.String(250))
    birth = database.Column(database.String(50))
    type = database.Column(database.Integer)


class User_Computer(database.Model, UserMixin):
    id = database.Column(database.String(50), primary_key = True)
    name = database.Column(database.String(250))
    email = database.Column(database.String(250), unique = True)
    birth = database.Column(database.String(50))
    type = database.Column(database.Integer)