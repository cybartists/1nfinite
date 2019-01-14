from flask import request, flash, render_template, redirect, url_for, jsonify
from app.api import api
from app import base


@api.route('/login', methods=['POST'])
def login():
    form = request.form
    if 'admin' == form['username'] and 'admin' == form['password']:
        return jsonify({'status': 0})
    else:
        return jsonify({'status': 1})

