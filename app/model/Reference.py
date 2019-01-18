#!/usr/bin/python
# -*- coding:utf-8 -*-
from sqlalchemy import Column,INT,VARCHAR,Text,Boolean,TIMESTAMP
from sqlalchemy.orm import relationship

from app.base.extensions import Base



class Reference(Base):
    __tablename__ = 'reference'
    id =Column(INT,primary_key=True)
    user_id = Column(INT)
    channel_id = Column(INT)
    topic_id = Column(INT)
    topic_artical_id = Column(INT)
    is_readed = Column(INT)
    create_time =Column(TIMESTAMP)
    status = Column(INT)