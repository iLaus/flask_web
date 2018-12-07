# -*- coding: utf-8 -*-
#!/usr/bin/python

from flask_restful import Api, Resource

from .apis import AuthCenter
from . import auth


api = Api(auth)
api.add_resource(AuthCenter, '', endpoint="auth_center")



