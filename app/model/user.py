from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,Text
from app.base.extensions import db


class User(db.Model):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String(255))

    def __repr__(self):
        return "User(username:%s)" % self.username

