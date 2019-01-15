from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from .config import Config


class Extensions:
    db = SQLAlchemy()
    moment = Moment()
    login_manager = LoginManager()
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'

    def init_app(self, app):
        self.db.init_app(app)
        self.moment.init_app(app)
        self.login_manager.init_app(app)
        CSRFProtect(app)

        engine = self.db.create_engine(Config.DB_URI)

        con = engine.connect()

        result = con.execute('show databases')
        print(result.fetchone())



