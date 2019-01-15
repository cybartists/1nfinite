from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from .config import Config

db = SQLAlchemy()
moment = Moment()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


class Extensions:

    @staticmethod
    def init_app(app):
        db.init_app(app)
        moment.init_app(app)
        login_manager.init_app(app)
        CSRFProtect(app)



