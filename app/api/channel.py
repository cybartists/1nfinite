from flask import request, flash, render_template, redirect, url_for, jsonify, session
from app.api import api
from app.base.extensions import DBSession
from flask import request, flash, render_template, redirect, url_for, jsonify, session

from app.model import Like, Channel, Image, User, Following, Reference
from app.base.function import sort_by_time, pd_time, is_admin, is_login



@api.route('/channel/like', methods=['POST'])
def like():
    if not is_login():
        return jsonify({'status': 2, 'message': '没有登录'})
    id = request.values.get('id', default=0, type=int)
    if id == 0:
        return jsonify({'status': 1, 'message': '错误的id'})

    db = DBSession()
    try:
        channel = db.query(Channel).filter(Channel.id == id).first()
        if channel is not None:
            like = Like(user_id=session.get(''))

    except Exception as e:
        db.close()
        return jsonify({
            'status': 1,
            'message': str(e),
            'error_message': str(e)
        })


@api.route('/channel/listdynamic', methods=['POST'])
def listAll():
    page = request.values.get('page', default=1, type=int)
    db_session = DBSession()
    try:
        query = db_session.query(Channel)

        count = query.count()
        channels = query.order_by(Channel.create_time.desc()).limit(10).offset((page - 1) * 10).all()
        is_end = (page*10 >= count)

        data = []
        for i in channels:
            user = db_session.query(User).filter(User.id == i.user_id).first()
            avatar = None
            if user.avatar_id != 0:
                image = db_session.query(Image).filter(Image.id == user.avatar_id).first()
                avatar = image.url
            if user.avatar_id == 0:
                avatar = 'http://127.0.0.1:5000/web/static/asset/chisec/avator.jpg'
            media = None
            if i.image_id != None and i.image_id != '':
                image = db_session.query(Image).filter(Image.id == i.image_id).first()
                media = image.url

            data.append({
                'id': i.id,
                'user_id': user.id,
                'content': i.content,
                'channel_name': user.channel_name,
                'username': user.username,
                'avatar': avatar,
                'media': media,
                'create_time': pd_time(i.create_time)
            })

        db_session.close()
        if is_end:
            return jsonify({
                'status': 2,
                'message': '没有更多消息了',
                'data': data
            })
        else:
            return jsonify({
                'status': 0,
                'message': 'ok',
                'data': data
            })
    except Exception as e:
        db_session.close()
        return jsonify({
            'status': 1,
            'message': str(e),
            'error_message': str(e)
        })

