# -*- coding: utf-8 -*-
#!/usr/bin/python

from flask import Blueprint
auth = Blueprint('auth', __name__)
from . import urls
