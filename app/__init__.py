from flask import Flask, redirect, render_template
from app.base.config import Config
from app.base.extensions import config_extensions

from app.api import api
from app.web import web
from app.admin import admin


def create_app():
    #创建实例
    app = Flask(__name__)
    #初始化配置
    app.config.from_object(Config)
    # #调用初始化方法
    Config.init_app(app)
    #错误页面显示
    config_errorhandler(app)
    #调用扩展方法 完成 app跟扩展对象的绑定
    config_extensions(app)

    #完成蓝本的注册
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(web, url_prefix='/web')
    app.register_blueprint(admin, url_prefix='/admin')

    @app.route('/')
    def index():
        return redirect('/web')

    return app


def config_errorhandler(app):
    @app.errorhandler(404)
    def page_not_found():
        return render_template('error/404.html')
