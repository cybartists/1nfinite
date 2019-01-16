from sqlalchemy import Column,INT,VARCHAR,Text,Boolean
from sqlalchemy.orm import relationship

from app.base.extensions import Base


class Following(Base):
    __tablename__ = 'Following'
    id = Column(INT, primary_key=True, autoincrement=True)
    user_id = Column(INT)
    Channel_user_id = Column(INT)
    Topic_id = Column(INT)
    status = Column(INT)