from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_uploads import UploadSet,IMAGES,configure_uploads,patch_request_class

#创建对象

db = SQLAlchemy()
moment = Moment()
# photos = UploadSet('photos',IMAGES)

#完成对象 跟 实例的绑定

def config_extensions(app):
    db.init_app(app)
    moment.init_app(app)

    # configure_uploads(app, photos)
    patch_request_class(app,size=None)
