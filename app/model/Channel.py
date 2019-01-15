from sqlalchemy import Column,INT,VARCHAR,Text,Boolean,ForeignKey
from sqlalchemy.orm import relationship

from app.base.extensions import Base


class Channel(Base):
    __tablename__ = 'Channel'
    id = Column(INT, primary_key=True, autoincrement=True)
    user_id = Column(INT,ForeignKey("user.id"))
    Content = Column(Text)
