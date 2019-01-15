from flask import render_template, url_for
from app.admin import admin


@admin.route('/')
def index():
    return render_template('admin_index.html')

@admin.route('/visitor/')
def course():
    return render_template('admin_visitor.html')


