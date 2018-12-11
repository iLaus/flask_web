# -*- coding: utf-8 -*-
#!/usr/bin/python

from flask import Blueprint

users_api = Blueprint('users', __name__)

# 模板路径可以添加到蓝图中
# template_folder='/opt/auras/templates/',   #指定模板路径
# static_folder='/opt/auras/flask_bootstrap/static/',#指定静态文件路径

from apps.users import urls
