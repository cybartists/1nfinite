from sqlalchemy import Column,INT,VARCHAR,Text,Boolean
from sqlalchemy.orm import relationship

from app.base.extensions import Base


class Topic(Base):
    __tablename__ = 'Topic'
    id = Column(INT, primary_key=True, autoincrement=True)
    user_id = Column(VARCHAR(255))
    nickname = Column(VARCHAR(255))
    sex = Column(INT)
    admin = Column(INT)
    ban = Column(INT)
    email = Column(VARCHAR(255))
    password = Column(VARCHAR(255))


    def find_user(self,form):
        if form['username'] == 'yyy' and form['password'] == 'zzz':
            return True