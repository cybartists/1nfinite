from werkzeug.security import generate_password_hash,check_password_hash


def password_encode(password):
    return generate_password_hash(password)


def password_auth(password_to_be_checked, password):
    return check_password_hash(password, password_to_be_checked)
