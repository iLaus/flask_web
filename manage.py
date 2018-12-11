# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
from app import create_app
from app import db as db_
from apps.users.models import User, Role
from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db_)


def make_shell_context():
    return dict(app=app, db=db_, User=User, Role=Role)


# manager.add_command("runserver", Server(host='192.168.1.30', port=80, use_debugger=True, use_reloader=True))
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
