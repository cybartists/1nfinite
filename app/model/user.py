from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,Text
from app.base.extensions import db

session = db.session
class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    nickname = db.Column(db.String)
    sex = db.Column(db.Boolean)
    admin = db.Column(db.Integer)
    ban = db.Column(db.Integer)
    email = db.Column(db.String)
    password = db.Column(db.String)
    def find_user(self,form):
        if form['username'] == 'yyy' and form['password'] == 'zzz':
            return True

    def add_User(self,form):
        p1 = User(username=form['username'], nickname=['nickname'], admin=form['admin'], password=form['password'],
                  ban=form['ban'], email=form['email'], sex=form['sex'])
        session.add_all([p1])
        session.commit()
    def __repr__(self):
        return "User(id:%d,username:%s,nickname:%s,admin:%d,ban:%int,email:%s,password:%s)" %(self.id,self.username,self.nickname,self.admin,self.ban,self.email,self.password)
