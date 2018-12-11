# -*- coding: utf-8 -*-
#!/usr/bin/python
from flask import Flask
from config.config import config

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, static_url_path='/statics', root_path=config[config_name].STATIC_ROOT)

    # 可以直接把对象里面的配置数据转换到app.config里面
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # app.config["DEBUG"] = False

    # 蓝图里面的url_prefix只需要写一个就好， 这里写了， app里面就不要写了， 这里会覆盖app里面的。
    # eg: user的路由， domain:port/users/user_center
    from apps.evaluation import evaluation as evaluation_app
    from apps.auth import auth as auth_app
    from apps.users import users_api as users_app
    app.register_blueprint(evaluation_app, url_prefix='/evaluation')
    app.register_blueprint(auth_app, url_prefix='/auths')
    app.register_blueprint(users_app, url_prefix='/users')

    # init_ext(app)
    db.init_app(app)

    # migrate.init_app(app)
    return app










