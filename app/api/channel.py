#!/usr/bin/python
# -*- coding:utf-8 -*-

from app.api import api
from app.base.extensions import DBSession
from flask import request, flash, render_template, redirect, url_for, jsonify, session

from app.model import Like, Channel, Image, User, Follow, Reference
from app.base.function import pd_time, is_admin, is_login, get_login_user, login_required


@api.route('/channel/new_message', methods=['POST'])
@login_required
def channel_new_message():
    user = get_login_user()
    content = request.form['content']
    image_id = request.values.get('image_id', default=0, type=int)

    if content == '':
        return jsonify({'status': 2})
    if user.ban == 1:
        return jsonify({
            'status': 1,
            'message': '你被禁言了，无法发送！'
        })

    if image_id == 0:
        image_id = None

    db = DBSession()
    try:
        channel = Channel(content=content, image_id=image_id, user_id=user.id)
        db.add(channel)
        db.commit()
        db.close()
        return jsonify({
            'status': 0,
            'message': '发出去辣'
        })
    except Exception as e:
        db.close()
        return jsonify({
            'status': 2,
            'message': str(e)
        })


@api.route('/channel/like', methods=['POST'])
@login_required
def channel_like():
    user = get_login_user()
    channel_id = request.values.get('id', default=0, type=int)
    if channel_id == 0:
        return jsonify({'status': 1, 'message': '错误的id'})

    db = DBSession()
    try:
        channel = db.query(Channel).filter(Channel.id == channel_id).first()
        if channel is not None:
            liked = db.query(Like).filter(Like.user_id == user.id, Like.channel_id == channel_id).first()
            if liked is not None:
                db.delete(liked)
                db.commit()
                like_count = db.query(Like).filter(Like.channel_id == channel_id).count()
                return jsonify({
                    'status': -1,
                    'message': 'ok',
                    'data': {'like_count': int(like_count)}
                })
            else:
                like = Like(user_id=user.id, status=1, channel_id=channel_id)
                db.add(like)
                db.commit()
                like_count = db.query(Like).filter(Like.channel_id == channel_id).count()
                return jsonify({
                    'status': 0,
                    'message': 'ok',
                    'data': {'like_count': int(like_count)}
                })
        else:
            return jsonify({
                'status': 1,
                'message': '消息可能已被删除'
            })
    except Exception as e:
        db.close()
        return jsonify({
            'status': 1,
            'message': str(e),
            'error_message': str(e)
        })


@api.route('/channel/follow')
@login_required
def follow():
    user = get_login_user()
    channel_user_id = request.values.get('id', default=0, type=int)
    if channel_user_id == 0:
        return jsonify({'status': 1, 'message': '错误的id'})

    db = DBSession()
    try:
        user = db.query(User).filter(User.id == channel_user_id).first()
        if user is not None:
            followed = db.query(Follow).filter(user_id=user.id, channel_user_id=channel_user_id).first()
            if followed is None:
                db.add(Follow(user_id=user.id, channel_user_id=channel_user_id, status=1))
                db.commit()
                return jsonify({
                    'status': 0,
                    'message': '关注成功'
                })
            else:
                db.delete(followed)
                db.commit()
                return jsonify({
                    'status': 0,
                    'message': '取关成功'
                })
        else:
            return jsonify({
                'status': 1,
                'message': '该用户不存在'
            })
    except Exception as e:
        db.close()
        return jsonify({
            'status': 1,
            'message': str(e),
            'error_message': str(e)
        })


@api.route('/channel/list_discovery', methods=['POST'])
def channel_dynamic_list():
    # if not is_login():
    #     return jsonify({'status': 2, 'message': '没有登录'})
    if is_login():
        curr_user = get_login_user()
    page = request.values.get('page', default=1, type=int)
    db = DBSession()
    try:
        query = db.query(Channel)

        count = query.count()
        channels = query.order_by(Channel.id.desc()).limit(10).offset((page - 1) * 10).all()
        is_end = (page * 10 >= count)

        data = []
        for channel in channels:
            user = db.query(User).filter(User.id == channel.user_id).first()
            avatar = None
            if user.avatar != '0':
                # image = db.query(Image).filter(Image.id == user.avatar_id).first()
                avatar = user.avatar
            if user.avatar == '0':
                avatar = '/web/static/asset/chisec/avator.jpg'
            media = None
            if channel.image_id is not None and channel.image_id is not '':
                image = db.query(Image).filter(Image.id == channel.image_id).first()
                media = image.url

            like_count = db.query(Like) \
                .filter(Like.channel_id == channel.id) \
                .count()
            if is_login():
                liked = db.query(Like) \
                    .filter(Like.channel_id == channel.id, Like.user_id == curr_user.id) \
                    .count()
                if liked > 0:
                    liked = True
                else:
                    liked = False
            else:
                liked = 0

            data.append({
                'id': channel.id,
                'user_id': user.id,
                'content': channel.content,
                'channel_name': user.channel_name,
                'username': user.username,
                'avatar': avatar,
                'media': media,
                'like_count': like_count,
                'liked': liked,
                'count': count,
                'create_time': pd_time(channel.create_time)
            })

        db.close()
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
        db.close()
        return jsonify({
            'status': 1,
            'message': '拉取失败',
            'error_message': str(e)
        })


@api.route('/channel/list_like', methods=['POST'])
@login_required
def list_like():
    user = get_login_user()
    page = request.values.get('page', default=1, type=int)
    db = DBSession()
    try:
        # 取本人点赞过的频道消息
        query = db.query(Channel) \
            .join(Like, Channel.id == Like.channel_id) \
            .filter(Like.user_id == user.id)

        count = query.count()
        channels = query.order_by(Channel.id.desc()).limit(10).offset((page - 1) * 10).all()
        is_end = (page * 10 >= count)

        data = []
        for channel in channels:
            user = db.query(User).filter(User.id == channel.user_id).first()
            avatar = None
            if user.avatar != '0':
                # image = db.query(Image).filter(Image.id == user.avatar_id).first()
                avatar = user.avatar
            if user.avatar == '0':
                avatar = '/web/static/asset/chisec/avator.jpg'
            media = None
            if channel.image_id is not None and channel.image_id is not '':
                image = db.query(Image).filter(Image.id == channel.image_id).first()
                media = image.url

            like_count = db.query(Like).filter(Like.channel_id == channel.id).count()
            # 都是点过赞的，直接值 True
            liked = True

            data.append({
                'id': channel.id,
                'user_id': user.id,
                'content': channel.content,
                'channel_name': user.channel_name,
                'username': user.username,
                'avatar': avatar,
                'media': media,
                'like_count': like_count,
                'liked': liked,
                'count': count,
                'create_time': pd_time(channel.create_time)
            })

        db.close()
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
        db.close()
        return jsonify({
            'status': 1,
            'message': '拉取失败',
            'error_message': str(e)
        })


@api.route('/channel/list_follow', methods=['POST'])
@login_required
def list_follow():
    user = get_login_user()
    page = request.values.get('page', default=1, type=int)
    db = DBSession()
    try:
        # 取本人订阅的频道主的最近消息
        query = db.query(Channel) \
            .join(Follow, Channel.user_id == Follow.channel_user_id) \
            .filter(Follow.user_id == user.id)

        count = query.count()
        channels = query.order_by(Channel.id.desc()).limit(10).offset((page - 1) * 10).all()
        is_end = (page * 10 >= count)

        data = []
        for channel in channels:
            user = db.query(User).filter(User.id == channel.user_id).first()
            avatar = None
            if user.avatar != '0':
                # image = db.query(Image).filter(Image.id == user.avatar_id).first()
                avatar = user.avatar
            if user.avatar == '0':
                avatar = '/web/static/asset/chisec/avator.jpg'
            media = None
            if channel.image_id is not None and channel.image_id is not '':
                image = db.query(Image).filter(Image.id == channel.image_id).first()
                media = image.url

            like_count = db.query(Like) \
                .filter(Like.channel_id == channel.id) \
                .count()
            if is_login():
                liked = db.query(Like) \
                    .filter(Like.channel_id == channel.id, Like.user_id == user.id) \
                    .count()
                if liked > 0:
                    liked = True
                else:
                    liked = False
            else:
                liked = 0

            data.append({
                'id': channel.id,
                'user_id': user.id,
                'content': channel.content,
                'channel_name': user.channel_name,
                'username': user.username,
                'avatar': avatar,
                'media': media,
                'like_count': like_count,
                'liked': liked,
                'count': count,
                'create_time': pd_time(channel.create_time)
            })

        db.close()
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
        db.close()
        return jsonify({
            'status': 1,
            'message': '拉取失败',
            'error_message': str(e)
        })
