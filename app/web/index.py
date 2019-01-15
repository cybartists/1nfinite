from flask import render_template, session
from app.web import web
from app.base.extensions import DBSession
from app.model.User import User


@web.route('/')
def index():
    dbs = DBSession()
    user_id = session.get('user_id')
    user = dbs.query(User).filter(User.id == user_id).first()
    dbs.close()
    login = False
    admin = False
    if user is not None:
        login = True
        if user.admin == 1:
            admin = True
        print('用户: ' + user.username + ' 访问。')

    return render_template('/index.html', login=login, admin=admin)
