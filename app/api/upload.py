from flask import request, flash, render_template, redirect, url_for, jsonify

from app.base.extensions import DBSession
from app.base.function import genreate_random_name
from app.api import api
from app import base
import os

from app.model import Image


@api.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    try:
        suffix = file.filename.rsplit('.', 1)[1]
        cwd = os.getcwd()
        url = genreate_random_name(12) + '.' + suffix
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
