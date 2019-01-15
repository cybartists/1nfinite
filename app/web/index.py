from flask import render_template, session
from app.web import web
from app.base.extensions import DBSession
from app.model.User import User


@web.route('/')
def index():
    dbs = DBSession()
    user_id = session.get('user_id')
    user = dbs.query(User.id == user_id).first()

    return render_template('/index.html', **user)
