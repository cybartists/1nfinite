from sqlalchemy import Column, INT, VARCHAR, TIMESTAMP
from app.base.extensions import Base


class Like(Base):
    __tablename__ = 'like'
    id = Column(INT, primary_key=True, autoincrement=True)
    user_id = Column(INT)
    status = Column(INT)
    channel_id = Column(INT)
    topic_artical_id = Column(INT)
    create_time = Column(TIMESTAMP)