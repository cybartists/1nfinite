from flask import render_template, url_for
from app.web import web
from app.model.user import User


@web.route('/')
def index():
    User()
    return render_template('/index.html')

