from flask import Flask, redirect
from app.base.config import Config
from app.base.extensions import Extensions

from app.api import api
from app.web import web
from app.admin import admin

config = Config()
extensions = Extensions()

app = Flask(__name__)
config.init_app(app)
extensions.init_app(app)

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(web, url_prefix='/web')
app.register_blueprint(admin, url_prefix='/admin')


# test



@app.route('/')
def index():
    return redirect('/web')


if __name__ == '__main__':
    app.run()
