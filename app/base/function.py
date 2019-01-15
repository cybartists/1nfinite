from werkzeug.security import generate_password_hash,check_password_hash
import re

def password_encode(password):
    return generate_password_hash(password)


def password_auth(password_to_be_checked, password):
    return check_password_hash(password, password_to_be_checked)


def correct_email(email_str):
    mail = re.compile('^www\.\w{1,15}@\w{1,10}\.(com|cn|net)$')
    if re.search(mail,email_str):
        return True
    else:
        return False