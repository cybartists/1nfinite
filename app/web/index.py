from flask import render_template, url_for
from app.web import web


@web.route('/')
def index():
    return render_template('/index.html')

