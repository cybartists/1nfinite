from sqlalchemy import Column,INT,VARCHAR,Text,Boolean,ForeignKey
from sqlalchemy.orm import relationship

from app.base.extensions import Base


class Topic(Base):
    __tablename__ = 'topic'
    id = Column(INT, primary_key=True, autoincrement=True)
    user_id = Column(INT,ForeignKey("user.id"))
    title = Column(Text)
    sum = Column(Text)

