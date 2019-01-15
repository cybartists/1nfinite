#decoding=utf-8
from flask import request, flash, render_template, redirect, url_for, jsonify
from app.api import api
from app import base


@api.route('/users/get_user', methods=['POST'])
def getUsers():
    form = request.form

    if 'username_example' == form['username'] and 'password_example' == form['password']:
        return jsonify({'status':0})
    else:
        return jsonify({'status':1})



@api.route('/users/create_user', methods=['POST'])
def createUsers():
    form = request.form
    try:
        username = form['username']
        password = form['password']
        email = form['email']
        sex = form['sex']
        nickname = form['nickname']
        #db操作
        if username == 'username_example':
            return jsonify({'status':2,'message':'用户名重复'})

        if email == 'email_example':
            return jsonify({'status': 3, 'message': '邮箱重复'})

        json = jsonify({'status':0,'message':'注册成功'})
        return json
    except Exception as e:
        print(e)
        return jsonify({'status':1,'message':'注册失败'})




@api.route('/users/update_user', methods=['POST'])
def updateUsers():
    pass


@api.route('/users/get_list', methods=['POST'])
def getList():
    pass
