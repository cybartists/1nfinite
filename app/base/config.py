import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    HOSTNAME = 'zhuangbi.party'
    PORT = '3306'
    DATABASE = 'test'
    USERNAME = 'root'
    PASSWORD = 'LfB9yOqj#ma&'
    DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}'.format(username=USERNAME, password=PASSWORD,
                                                                               host=HOSTNAME, port=PORT, db=DATABASE)

    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = True

    SECRET_KEY = 'F!tL%W^I64pkC2NHC!hsCC7q%z^Bft'

    @staticmethod
    def init_app(app):
        pass

