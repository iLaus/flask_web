# -*- coding: utf-8 -*-
#!/usr/bin/python

from flask import Blueprint
users = Blueprint('users', __name__, url_prefix='/users/api')
from . import urls
