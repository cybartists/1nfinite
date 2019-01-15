from sqlalchemy import Column,INT,VARCHAR,Text,Boolean
from sqlalchemy.orm import relationship

from app.base.extensions import Base


class Channel(Base):
    __tablename__ = 'Channel'
    id = Column(INT, primary_key=True, autoincrement=True)
    use_id = Column(INT)
    Content = Column(Text)
