from flask import render_template

from app.base.function import is_login, is_admin
from app.web import web


@web.route('/')
def index():
    return render_template('/index.html', login=is_login(), admin=is_admin())
