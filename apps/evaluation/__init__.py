# -*- coding: utf-8 -*-
#!/usr/bin/python

from flask import Blueprint
evaluation = Blueprint('evaluation', __name__)
from . import urls
