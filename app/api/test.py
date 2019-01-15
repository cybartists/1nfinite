from app.model.user import User

user = User()

form = {
    'username':'yyy',
    'password':'zzz',
    'nickname':'nick',
    'ban':1,
    'admin':1,
    'email':'mail',
    'sex':False
}
user.add_User(form)