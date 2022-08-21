from datetime import datetime as dt
import uuid as id
import hashlib
from flask_app.DB_Models import User, User_Computer
from . import database

utenti = None

#MAINTENANCE

def newHFid():
    """
    In:
        None
    Out:
        HFid
    """
    uid = id.uuid5(id.uuid4(), str(dt.timestamp(dt.now())))
    return str(uid)

def newId(name:str):
    """
    In:
        None
    Out:
        HFid
    """
    uid = id.uuid5(id.uuid4(), str(name))
    return str(uid)

def newVersion(last_version:str = None):
    y = dt.now().isocalendar().year
    w = dt.now().isocalendar().week
    d = dt.now().isocalendar().weekday
    v = str(y) + "." + str(w) + "." + str(d) + ".01"
    if last_version != None:
        if v[:-2] == last_version[:-2] and int(last_version[len(last_version) - 2:]) > 8:
            v = v[:-2] + str(int(last_version[len(last_version) - 2:]) + 1)
        elif v[:-2] == last_version[:-2] and int(last_version[len(last_version) - 2:]) <= 8:
            v = v[:-2] + "0" + str(int(last_version[len(last_version) - 2:]) + 1)
    return v

def s256(terms:str):
    """
    Quick way to calculate the sha256 of a string.
    In:
        terms:str
    Out:
        sha256:str
    """
    sha = hashlib.sha256(terms.encode("utf-8")).hexdigest()
    return sha

#SECURITY

def register(email:str, password:str, name:str, birth:str, type:int = 0):
    """
    Adds a user to the database and returns the relative HFid
    In:
        email, password, name, birth, type
    Out:
        user_info | Exception('Email already used')
    """
    HFid = newHFid()
    user = User.query.filter_by(email = email).first()
    
    if user:
        raise Exception("Email already used")
    
    new_user = User(HFid = HFid, name = name, email = email, password_hash = s256(email + password), birth = birth, type = 0) #type 0 user is the normal user
    database.session.add(new_user)
    database.session.commit()
    user_registered = User_Computer(id = HFid, name = name, email = email, birth = birth, type = 0)
    
    return user_registered

def login(email, password):
    """
    Checks if there is a match with a given email and password and eventually returns the HFid
    In:
        terms = [email, sha256(email + password)]
    Out:
        user_info | False | True(matched email)
    """
    user = User.query.filter_by(email = email).first()
    if user and user.password_hash == s256(email + password):
        user = User_Computer(id = user.HFid, name = user.name, email = email, birth = user.birth, type = user.type)
        return user
    elif user:
        return True
    return False

'''
def verify(HFid):
    """
    Checks if a user has a logged recently (max. 1 hour)
    In:
        HFid
    Out:
        True / False
    """
    cella = utenti.find(HFid, in_column = 1)
    if cella != None:
        last_verified = utenti.acell(('F' + str(cella.row)))
        if dt.timestamp(dt.now()) - int(last_verified.value) < 3600:
            return True
    return False
'''
#PERSONALIZATION
'''
def get_info(HFid:str):
    """
    Returns the information of an account
    In:
        HFid
    Out:
        [HFid, mail, name, birth, type] / False
    """
    cella = utenti.find(HFid)
    if cella != None:
        x = utenti.row_values(cella.row)
        return [x[0], x[1], x[3], x[4], x[6]]
    return False

def add_info(HFid:str, name:str, age:str):
    """
    Modifies the informations about a user
    In:
        name, birth
    Out:
        True / False
    """
    cella = utenti.find(HFid, in_column = 1)
    if cella != None:
        utenti.update(gspread.worksheet.rowcol_to_a1(cella.row, 4) + ":" + gspread.worksheet.rowcol_to_a1(cella.row, 5), [name, age])
        return True
    return False
'''