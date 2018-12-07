# -*- coding: utf-8 -*-
#!/usr/bin/python

from flask_restful import Api, Resource

from .apis import HelloWorld
from . import evaluation


api = Api(evaluation)
api.add_resource(HelloWorld, '/<string:todo_id>', endpoint="hello")





# evaluation.add_url_rule('/', 'hello', hello)