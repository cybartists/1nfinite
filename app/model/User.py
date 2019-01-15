from sqlalchemy import Column,INT,VARCHAR,Text,Boolean
from sqlalchemy.orm import relationship

from app.base.extensions import Base


class User(Base):
    __tablename__ = 'User'
    id = Column(INT, primary_key=True, autoincrement=True)
    email = Column(VARCHAR(255))
    username = Column(VARCHAR(255))
    admin = Column(INT)
    ban = Column(INT)


    nickname = Column(VARCHAR(255))
    sex = Column(INT)
    password = Column(VARCHAR(255))
