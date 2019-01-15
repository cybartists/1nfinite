from flask import render_template, url_for
from app.admin import admin


@admin.route('/')
def index():
    return render_template('admin_index.html')

@admin.route('/visitor/')
def visitor():
    return render_template('admin_visitor.html')
@admin.route('/user/')
def user():
    return render_template('admin_user.html')
@admin.route('/channel/')
def channel():
    return render_template('admin_channel.html')
@admin.route('/topic/')
def topic():
    return render_template('admin_topic.html')
@admin.route('/game/')
def game():
    return render_template('admin_game.html')


