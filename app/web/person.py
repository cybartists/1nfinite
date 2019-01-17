from flask import render_template, session, abort

from app.base.function import is_login, get_login_user
from app.web import web
from app.base.extensions import DBSession
from app.model.User import User


@web.route('/person/')
def person():
    return render_template('person.html', login=is_login())


@web.route('/person_follow/')
def person_follow():
    return render_template('person_follow.html', login=is_login())


@web.route('/person_like/')
def person_like():
    return render_template('person_like.html', login=is_login())


@web.route('/person_info/')
def person_info():
    if is_login():
        user = get_login_user()
        avatar = user.avatar
        if avatar == 0:
            avatar = '/web/static/asset/chisec/avator.jpg'
        return render_template('person_info.html',
                               username=user.username,
                               avatar=user.avatar,
                               channel_name=user.channel_name)
    else:
        abort(404)


@web.route('/person_about/')
def person_about():
    return render_template('person_about.html', login=is_login())
