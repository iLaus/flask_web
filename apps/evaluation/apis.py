# -*- coding: utf-8 -*-
#!/usr/bin/python


from flask_restful import Api, Resource

def hello():
    return 'hello world!'



class HelloWorld(Resource):
    todos = {}
    def get(self, todo_id):
        return {"result": todo_id}