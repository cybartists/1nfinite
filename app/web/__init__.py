from flask import Blueprint

web = Blueprint('web', __name__, static_folder='static', template_folder='templates')

from . import index
from . import person
from . import game