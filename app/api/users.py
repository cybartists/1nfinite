from flask import request, flash, render_template, redirect, url_for, jsonify
from app.api import api
from app import base


@api.route('/users/get_user', methods=['POST'])
def getUsers():
    pass


@api.route('/users/create_user', methods=['POST'])
def createUsers():
    pass


@api.route('/users/update_user', methods=['POST'])
def updateUsers():
    pass


@api.route('/users/get_list', methods=['POST'])
def getList():
    pass
