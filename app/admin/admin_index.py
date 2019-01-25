#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import render_template, url_for, abort, redirect
from app.base.function import is_admin
from app.admin import admin


@admin.route('/')
def index():
    if is_admin():
        return render_template('admin_index.html')
    return redirect('/')


@admin.route('/visitor/')
def visitor():
    if is_admin():
        return render_template('admin_visitor.html')
    return redirect('/')


@admin.route('/user/')
def user():
    if is_admin():
        return render_template('admin_user.html')
    return redirect('/')

@admin.route('/channel/')
def channel():
    if is_admin():
        return render_template('admin_channel.html')
    return redirect('/')

@admin.route('/topic/')
def topic():
    if is_admin():
        return render_template('admin_topic.html')
    return redirect('/')

@admin.route('/game/')
def game():
    if is_admin():
        return render_template('admin_game.html')
    return redirect('/')