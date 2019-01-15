from flask import render_template, session

from app.base.function import is_login, is_admin
from app.web import web
from app.base.extensions import DBSession
from app.model.User import User


@web.route('/')
def index():
    return render_template('/index.html', login=is_login(), admin=is_admin())
