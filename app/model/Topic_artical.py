from sqlalchemy import Column,INT,VARCHAR,Text,Boolean,ForeignKey
from sqlalchemy.orm import relationship

from app.base.extensions import Base


class Topic_artical(Base):
    __tablename__ = 'Topic_artical'
    id = Column(INT, primary_key=True, autoincrement=True)
    Topic_id = Column(INT,ForeignKey("Topic.id"))
    title = Column(Text)
    content = Column(Text)
    sum = Column(Text)

