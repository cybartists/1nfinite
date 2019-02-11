#!/usr/bin/python3
# -*- coding:utf-8 -*-
from app import create_app
from flask_script import Manager, Server

app = create_app()
manager = Manager(app)


@manager.command
def debug():
    Server(debugger=True)


if __name__ == '__main__':
    manager.run()
