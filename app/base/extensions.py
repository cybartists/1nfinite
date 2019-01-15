from sqlalchemy import create_engine
from flask_moment import Moment
from flask_uploads import UploadSet,IMAGES,configure_uploads,patch_request_class
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import Config


#创建对象
Base = declarative_base()
engine = create_engine(Config.DB_URI)
DBSession = sessionmaker(bind=engine)
moment = Moment()
# photos = UploadSet('photos',IMAGES)

#完成对象 跟 实例的绑定

def config_extensions(app):
    # db.init_app(app)
    moment.init_app(app)

    # configure_uploads(app, photos)
    patch_request_class(app, size=None)
