from flask import Flask, redirect
from app.api import api
from app.web import web
from app.admin import admin

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(web, url_prefix='/web')
app.register_blueprint(admin, url_prefix='/admin')


@app.route('/')
def index():
    return redirect('/web')


if __name__ == '__main__':
    app.run()
