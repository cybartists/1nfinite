#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import render_template, redirect

from app.base.function import is_login, is_admin, get_login_user
from app.web import web


@web.route('/like')
def like():
    if is_login():
        user = get_login_user()
        return render_template('/like.html',
                               login=True,
                               admin=is_admin(),
                               username=user.username,
                               channel_name=user.channel_name)
    else:
        return redirect('/')
