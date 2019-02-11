#!/usr/bin/python3
# -*- coding:utf-8 -*-
from flask import Flask, redirect, render_template
from app.base.config import Config
from app.base.extensions import config_extensions

from app.api import api
from app.web import web
from app.admin import admin


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    Config.init_app(app)

    # config_errorhandler(app)

    config_extensions(app)

    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(web, url_prefix='/web')
    app.register_blueprint(admin, url_prefix='/admin')

    @app.route('/')
    def index():
        return redirect('/web')

    return app


# def config_errorhandler(app):
#     @app.errorhandler(404)
#     def page_not_found():
#         return render_template('error/404.html')
