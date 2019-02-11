#!/usr/bin/python3
# -*- coding:utf-8 -*-
from app.base.extensions import DBSession
from app.model.User import User

session = DBSession()

new_user = User(username='admin', password='admin')

session.add(new_user)

session.commit()
session.close()

