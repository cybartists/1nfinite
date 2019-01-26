#!/usr/bin/python
# -*- coding:utf-8 -*-
from sqlalchemy import Column, INT, VARCHAR, TIMESTAMP, text
from app.base.extensions import Base


class Like(Base):
    __tablename__ = 'like'
    id = Column(INT, primary_key=True, autoincrement=True)
    user_id = Column(INT)
    status = Column(INT)
    channel_id = Column(INT)
    topic_artical_id = Column(INT)
    create_time = Column(TIMESTAMP(True), nullable=False, server_default=text('NOW()'))
