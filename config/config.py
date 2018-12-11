# -*- coding: utf-8 -*-
#!/usr/bin/python

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DB_USER = os.environ.get("DB_USER") or "postgres"
DB_PWD = os.environ.get("DB_PWD") or "postgres"
DB_DOMAIN = os.environ.get("DB_DOMAIN") or "localhost"
DB_PORT = os.environ.get("DB_PORT") or "5432"
DB_DATABASE = os.environ.get("DB_DATABASE") or "flask_web"


class Config:
    STATIC_ROOT = os.path.dirname(BASE_DIR)

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(DB_USER, DB_PWD, DB_DOMAIN, DB_PORT, DB_DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod

    # // 此注释可表明使用类名可以直接调用该方法

    def init_app(app):
        pass
        # 执行当前需要的环境的初始化



class DevelopmentConfig(Config):


    # 开发环境
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #                           'sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite')



class TestingConfig(Config):


    # 测试环境
    TESTING = True



class ProductionConfig(Config):


    # 生产环境
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}