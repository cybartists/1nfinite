#!/usr/bin/python3
# -*- coding:utf-8 -*-
import string
import random
from functools import wraps

from werkzeug.security import generate_password_hash, check_password_hash
from flask import session, jsonify
from app.base.extensions import DBSession
from app.model.User import User
import re
import datetime


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


def set_login(user):
    session.permanent = True
    session['user_id'] = user.id


def set_logout():
    session.pop('user_id')


def is_login():
    user_id = session.get('user_id')
    return user_id is not None


def get_login_user():
    if is_login():
        dbs = DBSession()
        user_id = session.get('user_id')
        user = dbs.query(User).filter(User.id == user_id).first()
        dbs.close()
        return user
    else:
        return None


def is_admin():
    dbs = DBSession()
    user_id = session.get('user_id')
    user = dbs.query(User).filter(User.id == user_id).first()
    dbs.close()
    if user is not None:
        if user.admin == 1:
            return True
    return False


def pd_time(time):
    # sec = (datetime.datetime.now() - time).seconds
    # if sec < 60:
    #     return str(sec) + '秒前'
    # else:
    #     minute = sec / 60
    #     if minute < 60:
    #         return str(int(minute)) + '分钟前'
    #     else:
    #         hour = minute / 60
    #         if hour < 24:
    #             return str(int(hour)) + '小时前'
    #         else:
    #             days = hour / 24
    #             if days < 7:
    #                 return str(int(days)) + '天前'
    #             else:
                    return time.strftime('%Y年%m月%d日 %H时%M分%S秒')


def generate_random_name(length=10):
    a = ''
    s = random.sample(string.ascii_letters + string.digits, length)
    for i in s:
        a += i
    return a


# decorators:

def login_required(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        if is_login():
            return fun(*args, **kwargs)
        else:
            return jsonify({
                'status': 1,
                'message': '请先登录'
            })
    return wrapper


def admin_required(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        if is_admin():
            return fun(*args, **kwargs)
        else:
            return jsonify({
                'status': 1,
                'message': '没有权限'
            })
    return wrapper
