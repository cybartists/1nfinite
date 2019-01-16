from flask import request, flash, render_template, redirect, url_for, jsonify, session
from app.api import api
from app.base.extensions import DBSession
from flask import request, flash, render_template, redirect, url_for, jsonify, session
from app.model.Channel import Channel
from app.model.Reference import Reference
from app.base.function import sort_by_time

@api.route('/channel/listFirst')
def listChannel():
    try:
        if session['user_id'] ==None or session['user_id'] =='':
            return jsonify({'status':2,'message':'没有登录'})
        userid = session['user_id']
        db_session = DBSession()
        data = db_session.query(Reference).filter_by(user_id=userid).all()
        sort_by_time(data)
        if len(data)<=10:
            for i in data:
                pass
    except Exception as e:
        return jsonify({'status':1,'message':'获取失败'})