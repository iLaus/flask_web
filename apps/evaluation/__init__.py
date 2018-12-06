from flask import Blueprint
evaluation = Blueprint('evaluation', __name__, url_prefix='/evaluation/api/v0.1')
from . import urls
