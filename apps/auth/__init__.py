# -*- coding: utf-8 -*-
#!/usr/bin/python

from flask import Blueprint
auth = Blueprint('auth', __name__, url_prefix='/auth/api')
from . import urls
