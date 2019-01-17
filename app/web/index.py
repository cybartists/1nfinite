from flask import render_template

from app.base.function import is_login, is_admin, get_login_user
from app.web import web


@web.route('/')
def index():
    if is_login():
        user = get_login_user()
        return render_template('/index.html',
                               login=True,
                               admin=is_admin(),
                               username=user.username,
                               channel_name=user.channel_name)
    else:
        return render_template('/index.html',
                               login=False,
                               admin=False,
                               username=None)
