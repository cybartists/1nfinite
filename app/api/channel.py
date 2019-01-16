from flask import request, flash, render_template, redirect, url_for, jsonify, session
from app.api import api
from app.base.extensions import DBSession
from flask import request, flash, render_template, redirect, url_for, jsonify, session
from app.model.Channel import Channel
from app.model.Reference import Reference
from app.base.function import sort_by_time, pd_time


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
                channel_create_time = pd_time(i.create_time)
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
        return jsonify({'status': 1, 'message': '获取失败'})

@api.route('/channel/followlist',methods=['POST'])
def listChannelFollow():
    try:
        if session['user_id'] == None or session['user_id']=='':
            return jsonify({'status': 2, 'message': '没有登录'})
        pass
    except Exception as e:
        return jsonify({'status':1,'message':"获取失败",'data':{},'error_message':str(e)})