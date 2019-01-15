from flask import render_template, url_for
from app.web import web
from app.model.User import User


@web.route('/')
def index():
    return render_template('/index.html')

