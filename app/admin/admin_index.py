# -*- coding:utf-8 -*-
from flask import render_template, url_for, abort
from app.base.function import is_admin
from app.admin import admin


@admin.route('/')
def index():
    if is_admin():
        return render_template('admin_index.html')
    abort(404)


@admin.route('/visitor/')
def visitor():
    if is_admin():
        return render_template('admin_visitor.html')
    abort(404)


@admin.route('/user/')
def user():
    if is_admin():
        return render_template('admin_user.html')
    abort(404)


@admin.route('/channel/')
def channel():
    if is_admin():
        return render_template('admin_channel.html')
    abort(404)


@admin.route('/topic/')
def topic():
    if is_admin():
        return render_template('admin_topic.html')
    abort(404)


@admin.route('/game/')
def game():
    if is_admin():
        return render_template('admin_game.html')
    abort(404)
