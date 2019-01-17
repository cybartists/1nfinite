from datetime import datetime

from sqlalchemy import Column,INT,VARCHAR,Text,Boolean,ForeignKey,TIMESTAMP


from app.base.extensions import Base


class Channel(Base):
    __tablename__ = 'channel'
    id = Column(INT, primary_key=True, autoincrement=True)
    user_id = Column(INT)
    content = Column(Text)
    image_id = Column(INT)
    create_time = Column(TIMESTAMP, default=datetime.now())#时间戳模型
