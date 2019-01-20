# -*- coding:utf-8 -*-
from flask import request, flash, render_template, redirect, url_for, jsonify

from app.base.extensions import DBSession
from app.base.function import generate_random_name, is_login, get_login_user
from app.api import api
from app import base
import os

from app.model import Image, User


@api.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    try:
        suffix = file.filename.rsplit('.', 1)[1]
        cwd = os.getcwd()
        url = generate_random_name(12) + '.' + suffix
        file.save(os.path.join(cwd + '/app/api/static/upload/' + url))
        db = DBSession()
        image = Image(url='/api/static/upload/' + url)
        db.add(image)
        db.commit()
        url = image.url
        image_id = image.id
        db.close()
        return jsonify({
            'status': 0,
            'message': '保存成功',
            'data': {
                'image_id': image_id,
                'url': url
            }
        })
    except Exception as e:
        return jsonify({'status': 1, 'message': '保存失败:'+str(e)})


@api.route('/upload_avatar', methods=['POST'])
def upload_avatar():
    if not is_login():
        return jsonify({'status': 1, 'message': '保存失败:'})
    user = get_login_user()
    file = request.files['file']
    try:
        suffix = file.filename.rsplit('.', 1)[1]
        cwd = os.getcwd()
        url = generate_random_name(12) + '.' + suffix
        file.save(os.path.join(cwd + '/app/api/static/upload/' + url))
        db = DBSession()
        user = db.query(User).filter(User.id == user.id).first()
        user.avatar = '/api/static/upload/' + url
        db.commit()
        url = user.avatar
        db.close()
        return jsonify({
            'status': 0,
            'message': '保存成功',
            'data': {
                'url': url
            }
        })
    except Exception as e:
        return jsonify({'status': 1, 'message': '保存失败:'})
