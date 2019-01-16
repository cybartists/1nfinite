from flask import request, flash, render_template, redirect, url_for, jsonify, session
from app.api import api
from app.base.extensions import DBSession
from flask import request, flash, render_template, redirect, url_for, jsonify, session
from app.model.Channel import Channel
from app.model.Following import Following
from app.model.Reference import Reference
from app.base.function import sort_by_time, pd_time

@api.route('/channel/listdynamic',methods=['POST'])
def listAll():
    try:
        db_session = DBSession()
        data = db_session.query(Channel).order_by(Channel.create_time.desc()).all()
        Channel_list_arr = []
        for i in data:
            Channel_list = {}
            id = i.id
            user_id = i.user_id
            username = db_session.query(User).filter(id=user_id).first().username
            Content = i.Content
            create_time = pd_time(i.create_time)
            Channel_list.update(
                {
                    'id':id,
                    'user_id':user_id,
                    'Content':Content,
                    'create_time':create_time
                }
            )
            Channel_list_arr.append(Channel_list)
            db_session.close()
        return jsonify({'status':0,'message':'获取成功','data':Channel_list_arr})
    except Exception as e :
        return jsonify({'status':1,'message':'获取失败','error_message':str(e)})



















@api.route('/channel/referencelist',methods=['POST'])
def listChannelReference():
    try:
        if session['user_id'] == None or session['user_id'] == '':
            return jsonify({'status': 2, 'message': '没有登录'})
        userid = session['user_id']
        page_num = request.form['page']
        page_cur = (page_num - 1) * 10
        db_session = DBSession()
        channel_dict_arr = []
        data = db_session.query(Reference).filter_by(user_id=userid).order_by(Reference.create_time.desc()).limit(
            11).offset(page_cur).all()
        # sort_by_time(data)
        if len(data) <= 10:
            for i in data:
                channel_dict = {}
                channel_id = i.id
                channel_content = i.content
                channel_userid = i.user_id
                channel_status = i.status
                channel_topic_id = i.topic_id
                channel_topic_artical_id = i.topic_artical_id
                channel_create_time = pd_time(i.create_time)
                channel_dict.update(
                    {
                        'channel_id': channel_id,
                        'channel_content': channel_content,
                        'channel_userid': channel_userid,
                        'channel_create_time': channel_create_time,
                        'reference_status':channel_status,
                        'topic_artical_id':channel_topic_artical_id,
                        'topic_id':channel_topic_id
                    }
                )
                channel_dict_arr.append(channel_dict)
            db_session.close()
            return jsonify({'status': 2, 'message': '最后一页了', 'data': channel_dict_arr})
        for i in range(10):
            channel_dict = {}
            channel_id = data[i].id
            channel_content = data[i].content
            channel_userid = data[i].user_id
            channel_status = data[i].status
            channel_topic_id = data[i].topic_id
            channel_topic_artical_id = data[i].topic_artical_id
            channel_create_time = pd_time(data[i].create_time)
            channel_dict.update(
                {
                    'channel_id': channel_id,
                    'channel_content': channel_content,
                    'channel_userid': channel_userid,
                    'channel_create_time': channel_create_time,
                    'reference_status': channel_status,
                    'topic_artical_id': channel_topic_artical_id,
                    'topic_id': channel_topic_id
                }
            )
            channel_dict_arr.append(channel_dict)
        db_session.close()
        return jsonify({'status': 0, 'message': '获取成功', 'data': channel_dict_arr})
    except Exception as e:
        return jsonify({'status': 1, 'message': '获取失败'})

@api.route('/channel/followlist',methods=['POST'])
def listChannelFollow():
    try:
        if session['user_id'] == None or session['user_id']=='':
            return jsonify({'status': 2, 'message': '没有登录'})
        userid = session['user_id']
        page_num = request.form['page']
        page_cur = (page_num - 1) * 10
        db_session = DBSession()
        channel_dict_arr = []
        data = db_session.query(Following).filter_by(user_id=userid).order_by(Reference.create_time.desc()).limit(
            11).offset(page_cur).all()
        # sort_by_time(data)
        if len(data) <= 10:
            for i in data:
                channel_dict = {}
                channel_id = i.id
                channel_Channel_user_id = i.Channel_user_id
                channel_userid = i.user_id
                channel_Topic_id = i.Topic_id
                channel_create_time = pd_time(i.create_time)
                channel_dict.update(
                    {
                        'channel_id': channel_id,
                        'Channel_user_id': channel_Channel_user_id,
                        'channel_userid': channel_userid,
                        'channel_create_time': channel_create_time,
                        'Topic_id':channel_Topic_id
                    }
                )
                channel_dict_arr.append(channel_dict)
            db_session.close()
            return jsonify({'status': 2, 'message': '最后一页了', 'data': channel_dict_arr})
        for i in range(10):
            channel_dict = {}
            channel_id = data[i].id
            channel_content = data[i].content
            channel_userid = data[i].user_id
            channel_create_time = pd_time(data[i].create_time)
            channel_dict.update(
                {
                    'channel_id': channel_id,
                    'channel_content': channel_content,
                    'channel_userid': channel_userid,
                    'channel_create_time': channel_create_time
                }
            )
            channel_dict_arr.append(channel_dict)
        db_session.close()
        return jsonify({'status': 0, 'message': '获取成功', 'data': channel_dict_arr})
    except Exception as e:
        return jsonify({'status':1,'message':"获取失败",'data':{},'error_message':str(e)})