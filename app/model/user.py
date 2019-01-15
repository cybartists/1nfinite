from sqlalchemy import Column,INT,VARCHAR,Text,Boolean
from sqlalchemy.orm import relationship

from app.base.extensions import Base


class User(Base):
    __tablename__ = 'User'
    id = Column(INT, primary_key=True, autoincrement=True)
    username = Column(VARCHAR(255))
    nickname = Column(VARCHAR(255))
    sex = Column(INT)
    admin = Column(INT)
    ban = Column(INT)
    email = Column(VARCHAR(255))
    password = Column(VARCHAR(255))


    def find_user(self,form):
        if form['username'] == 'yyy' and form['password'] == 'zzz':
            return True