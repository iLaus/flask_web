# -*- coding: utf-8 -*-
#!/usr/bin/python
from flask import Flask
from config.settings import settings

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from apps.evaluation import evaluation as evaluation_app
from apps.auth import auth as auth_app


app = Flask(__name__, static_url_path='/statics',root_path=settings.STATIC_ROOT)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(evaluation_app)
app.register_blueprint(auth_app)


manager = Manager(app)
manager.add_command('db', MigrateCommand)



if __name__ == '__main__':
    manager.debug = True
    manager.run()
    # manager.run(host='0.0.0.0')





