# -*- coding: utf-8 -*-
#!/usr/bin/python
import uuid

from flask_restful import Api, Resource, reqparse
from .models import User, Role
from app import db



class UserCenter(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type = str, location='json')
        self.reqparse.add_argument('password', type = str, location='json')
        super(UserCenter, self).__init__()

    def get(self):
        return {"auth_token": "111".join(str(uuid.uuid1()).split("-"))}

    def post(self):
        # 用户注册
        try:
            data = self.reqparse.parse_args()
            if data.get("username") and data.get("password"):
                print (data)
                user = User(**data)
                db.session.add(user)
                db.session.commit()
                return {"status": "SUCC", "message": u"成功注册"}
            return {"status": "FAIL", "message": u"用户名和密码传入错误"}

        except Exception as ex:
            print("exception : {}".format(ex))
            return {"status": "FAIL", "message": u"注册失败"}

