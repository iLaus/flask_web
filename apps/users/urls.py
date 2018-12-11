# -*- coding: utf-8 -*-
#!/usr/bin/python

from flask_restful import Api, Resource

from .apis import UserCenter
from . import users_api


user_api = Api(users_api)
# users_api.add_resource(UserCenter, '/user_center', endpoint="user_center")
user_api.add_resource(UserCenter, '/user_center', endpoint="user_center")



