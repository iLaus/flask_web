# -*- coding: utf-8 -*-
#!/usr/bin/python
import uuid

from flask_restful import Api, Resource, reqparse
from .models import User, Role
from app import db



class UserCenter(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        # self.reqparse.add_argument('title', type = str, location = 'json')
        # self.reqparse.add_argument('description', type = str, location = 'json')
        # self.reqparse.add_argument('done', type = bool, location = 'json')
        super(UserCenter, self).__init__()

    def get(self):
        return {"auth_token": "111".join(str(uuid.uuid1()).split("-"))}

    def post(self):
        # 用户注册

        args = self.reqparse.parse_args()
        for key, value in args.iteritems():
            print(key, value)
            # if v != None:
                # task[k] = v
        pass
