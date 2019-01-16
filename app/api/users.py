# decoding=utf-8
from flask import request, flash, render_template, redirect, url_for, jsonify, session
from app.api import api
from app.base.extensions import DBSession
from app.base.function import password_encode, password_auth
from app.model.User import User
from app.model.Channel import Channel
from app.base.function import correct_email

sex_dict = {
    0: '未知',
    1: '男',
    2: '女',
    3: '女汉子',
    4: '女装大佬'
}
country_dict = {
    0:'霍格沃兹',
    1:'赛博坦',
    2:'瓦坎达',
    3:'新日暮里',
    4:'3栋501',
    5:'卡塞尔',
    6:'召唤师峡谷'
}

@api.route('/users/login', methods=['POST'])
def login():
    form = request.form
    if None == form['username'] or form['username'] == '':
        return jsonify({'status': 0, 'message': '请输入用户名！'})
    if None == form['password'] or form['password'] == '':
        return jsonify({'status': 1, 'message': '请输入密码！'})

    db_session = DBSession()
    user = db_session.query(User).filter(User.username == form['username']).first()
    db_session.close()

    if None is not user and password_auth(password_to_be_checked=form['password'], password=user.password):
        session['user_id'] = user.id
        return jsonify({'status': 2, 'message': '登录成功'})
    else:
        return jsonify({'status': 3, 'message': '登录失败'})


@api.route('/users/create', methods=['POST'])
def create():
    form = request.form
    try:
        username = form['username']
        if username == None or username == '':
            return jsonify({'status': 1, 'message': '用户名为空'})

        password = form['password']

        if password == None or password == '':
            return jsonify({'status': 2, 'message': '密码为空'})
        password_again = form['password_again']

        if password_again == None or password_again == '':
            return jsonify({'status': 3, 'message': '确认密码为空'})

        if password_again != password:
            return jsonify({'status': 3, 'message': '两次密码不同'})

        email = form['email']

        if email == None or email == '':
            return jsonify({'status': 4, 'message': '邮箱空'})
        if correct_email(email) == False:
            return jsonify({'status': 4, 'message': '邮箱格式错误'})

        # sex = form['sex']
        # nickname = form['nickname']

        # 密码加密
        password_encoded = password_encode(password)

        # db操作
        db_session = DBSession()

        user = db_session.query(User).filter(User.username == username).first()
        if user is not None:
            db_session.close()
            return jsonify({'status': 1, 'message': '用户名已存在'})

        email_db = db_session.query(User).filter(User.email == email).first()
        if email_db is not None:
            db_session.close()
            return jsonify({'status': 4, 'message': '邮箱重复'})

        user = User(username=username, password=password_encoded, email=email)
        session['user_id'] = user.id  # 自动登录
        db_session.add(user)
        db_session.commit()
        db_session.close()
        return jsonify({'status': 0, 'message': '注册成功'})
    except Exception as e:
        print(e)
        return jsonify({'status': 5, 'message': '未知错误'})


@api.route('/users/logout', methods=['POST'])
def logout():
    try:
        session['user_id'] = None
        return jsonify({'status': 0, 'message': '退出登录成功'})
    except Exception as e:
        return jsonify({'status': 1, 'message': '退出登录失败'})


@api.route('/users/update', methods=['POST'])
def updateUsers():
    try:
        if session['user_id'] == None or session['user_id'] == '':
            return jsonify({'status': 2, 'message': '没有登录'})
        else:
            form = request.form
            admin = form['admin']
            ban = form['ban']
            nickname = form['nickname']
            sex = form['sex']
            password = form['password']

            db_session = DBSession()
            user_id = session['user_id']
            user = db_session.query(User).filter_by(id=user_id).first()
            if admin != None and admin != '':
                user.admin = admin
            if ban != None and ban != '':
                user.ban = ban
            if nickname != None and nickname != '':
                user.nickname = nickname
            if sex != None and sex != '':
                user.sex = sex
            if password != '' and password != None:
                password_encoded = password_encode(password)

                user.password = password_encoded
            db_session.commit()
            db_session.close()
            return jsonify({'status': 0, 'message': '修改成功'})


    except Exception as e:
        print(e)
        return jsonify({'status': 1, 'message': '未知错误'})


@api.route('/users/list', methods=['POST'])
def getList():
    try:
        db_session = DBSession()
        page_num = int(request.form['page'])
        page_cur = (page_num-1)*10
        user_dict_list = []
        users = db_session.query(User).limit(11).offset(page_cur).all()
        if len(users)<=10:
            for i in users:
                user_dict = {}
                user_id = i.id
                user_username = i.username
                user_admin = i.admin
                user_ban = i.ban
                user_nickname = i.nickname
                user_sex = i.sex
                user_dict.update(
                    {
                        'id': user_id,
                        'username': user_username,
                        'admin': user_admin,
                        'ban': user_ban,
                        'nickname': user_nickname,
                        'sex': user_sex
                    }
                )
                user_dict_list.append(user_dict)

            return jsonify({'status':2,'message':'这是最后了','data':user_dict_list,'page':page_num})
        for i in range(10):
            user_dict = {}
            user_id = users[i].id
            user_username = users[i].username
            user_admin = users[i].admin
            user_ban = users[i].ban
            user_nickname = users[i].nickname
            user_sex = users[i].sex
            user_dict.update(
                {
                    'id':user_id,
                    'username':user_username,
                    'admin':user_admin,
                    'ban':user_ban,
                    'nickname':user_nickname,
                    'sex':user_sex
                }
            )
            user_dict_list.append(user_dict)
        session['user_page_count'] += 10
        db_session.close()
        return jsonify({'status':0,'message':'获取成功','data':user_dict_list,'page':page_num})
    except Exception as e:
        return jsonify({'status':1,'message':'获取失败','data':{},'error_message':str(e)})


@api.route('/user/listsex', methods=['POST'])
def listSex():
    try:
        return jsonify({'status': 0, 'message': '获取成功', 'data': sex_dict})
    except Exception as e:
        return jsonify({'status': 1, 'message': '获取失败', 'data': None})


@api.route('/users/sex', methods=['POST'])
def getSex():
    try:
        sex = request.form['sex']
        sex_code = sex_dict[sex]
        return jsonify({'status': 0, 'message': '获取成功', 'data': {sex_code: sex}})

    except Exception as e:
        return jsonify({'status': 1, 'message': '获取失败'})


@api.route('/users/channelcount', methods=['POST'])
def channelCount():
    try:
        db_session = DBSession()
        userid = session.get('user_id')
        # db操作

        # user = db_session.query(Channel).filter_by(user_id=userid).all()
        #
        # countNum = int(len(user))

        countNum = db_session.query(Channel).filter_by(user_id=userid).count()
        db_session.close()
        return jsonify({'status': 0, 'message': '获得数据成功', 'countNum': countNum})

    except Exception as e:
        print(e)
        return jsonify({'status': 1, 'message': '没有登录'})
