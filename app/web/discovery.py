#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import render_template, redirect

from app.base.function import is_login, is_admin
from app.web import web


@web.route('/discovery')
def discovery():
    if not is_login():
        return redirect('/web')
    return render_template('/discovery.html', login=is_login(), admin=is_admin())
