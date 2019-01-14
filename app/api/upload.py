from flask import request, flash, render_template, redirect, url_for, jsonify
from app.api import api
from app import base
@api.route('/upload',methods=['POST'])
def upload():
    pass