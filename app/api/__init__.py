from flask import Blueprint

api = Blueprint('api', __name__, static_folder='static')

# from . import login

from . import users,token,upload,channel,topic