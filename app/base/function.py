from werkzeug.security import generate_password_hash, check_password_hash
from flask import session
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
#时间戳排序
def sort_by_time(List):
    List.sort(key=lambda x:x.create_time,reverse=True)


def pd_time(time):
    sec = (datetime.datetime.now()-time).seconds
    if sec<60:
        return str(sec)+'秒前'
    else:
        minute = sec/60
        if minute <60:
            return str(int(minute))+'分钟前'
        else:
            hour = minute/60
            if hour<24:
                return str(int(hour))+'小时前'
            else:
                days = hour/24
                if days<7:
                    return str(int(days))+'天前'
                else:
                    return time.strftime('%Y年%m月%d日星期%w %H时%M分%S秒')