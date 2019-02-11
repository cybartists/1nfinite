#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    HOSTNAME = 'zhuangbi.party'
    PORT = '3306'
    DATABASE = '1finite'
    USERNAME = 'root'
    PASSWORD = 'LfB9yOqj#ma&'
    DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}'.format(username=USERNAME, password=PASSWORD,
                                                                               host=HOSTNAME, port=PORT, db=DATABASE)

    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 设置session 7天过期。
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

    DEBUG = True

    SECRET_KEY = 'F!tL%W^I64pkC2NHC!hsCC7q%z^Bft'

    @staticmethod
    def init_app(app):
        pass

