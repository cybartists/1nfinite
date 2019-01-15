from flask import request, flash, render_template, redirect, url_for, jsonify
from app.api import api
from app import base
import os
@api.route('/upload',methods=['POST'])
def upload():
    file = request.files.get('photo')
    if file:
        filename = file.filename
        cwd = os.getcwd()
        file.save(os.path.join(cwd,filename))
        return jsonify({'status':0,'message':'保存成功'})
    else:
        return jsonify({'status':1,'message':'保存失败'})
