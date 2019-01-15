# decoding=utf-8
from flask import request, flash, render_template, redirect, url_for, jsonify
from app.api import api
from app.base.extensions import DBSession
from app.base.function import password_encode, password_auth
from app.model.user import User


@api.route('/users/login', methods=['POST'])
def login():
    form = request.form
    if None  == form['username']or form['username'] == '':
        return jsonify({'status': 0, 'message': '请输入用户名！'})
    if None == form['password']or form['password'] == '':
        return jsonify({'status': 1, 'message': '请输入密码！'})

    session = DBSession()
    user = session.query(User).filter(User.username == form['username']).one()
    session.close()

    if None is not user and password_auth(password_to_be_checked=form['password'], password=user.password):
        return jsonify({'status': 2, 'message': '登录成功'})
    else:
        return jsonify({'status': 3, 'message': '登录失败'})


@api.route('/users/create', methods=['POST'])
def create():
    form = request.form
    try:
        username = form['username']
        password = form['password']
        email = form['email']
        # sex = form['sex']
        # nickname = form['nickname']

        # 密码加密
        password_encoded = password_encode(password)

        # db操作
        session = DBSession()

        user = session.query(User).filter(User.username == username).first()
        if user is not None:
            session.close()
            return jsonify({'status': 2, 'message': '用户名重复'})

        email = session.query(User).filter(User.email == email).first()
        if email is not None:
            return jsonify({'status': 3, 'message': '邮箱重复'})

        user = User(username=username, password=password_encoded)
        session.add(user)
        session.commit()
        session.close()

        return jsonify({'status': 0, 'message': '注册成功'})
    except Exception as e:
        print(e)
        return jsonify({'status': 1, 'message': '未知错误'})


@api.route('/users/update_user', methods=['POST'])
def updateUsers():
    pass


@api.route('/users/get_list', methods=['POST'])
def getList():
    pass
