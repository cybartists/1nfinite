from sqlalchemy import Column,INT,VARCHAR,Text,Boolean,TIMESTAMP
from sqlalchemy.orm import relationship

from app.base.extensions import Base



class Reference(Base):
    __tablename__ = 'Reference'
    user_id = Column(INT)
    channel_id = Column(INT)
    topic_id = Column(INT)
    topic_artical_id = Column(INT)
    is_readed = Column(INT)
    create_time =Column(TIMESTAMP)