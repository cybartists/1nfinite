from werkzeug.security import generate_password_hash, check_password_hash
from flask import session
from app.base.extensions import DBSession
from app.model.User import User
import re


def password_encode(password):
    return generate_password_hash(password)


def password_auth(password_to_be_checked, password):
    return check_password_hash(password, password_to_be_checked)


def correct_email(email_str):
    mail = re.compile('^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$')
    if re.search(mail, email_str):
        return True
    else:
        return False


def is_login():
    user_id = session.get('user_id')
    return user_id is not None


def is_admin():
    dbs = DBSession()
    user_id = session.get('user_id')
    user = dbs.query(User).filter(User.id == user_id).first()
    dbs.close()
    admin = False
    if user is not None:
        if user.admin == 1:
            admin = True
    return admin
