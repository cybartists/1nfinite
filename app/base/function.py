from werkzeug.security import generate_password_hash,check_password_hash
def password_hash(password):
    return generate_password_hash(password)