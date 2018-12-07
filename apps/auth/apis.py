# -*- coding: utf-8 -*-
#!/usr/bin/python
import uuid

from flask_restful import Api, Resource



class AuthCenter(Resource):

    def get(self):
        return {"auth_token": "".join(str(uuid.uuid1()).split("-"))}
