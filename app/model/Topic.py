from sqlalchemy import Column,INT,VARCHAR,Text,Boolean
from sqlalchemy.orm import relationship

from app.base.extensions import Base


class Topic(Base):
    __tablename__ = 'Topic'
    id = Column(INT, primary_key=True, autoincrement=True)
    user_id = Column(INT,)
    title = Column(Text)
    sum = Column(Text)

