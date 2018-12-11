# -*- coding: utf-8 -*-
#!/usr/bin/python

from app import db


class Permission:
    FOLLOW = 0x01
    COMMENT = 0x02
    WRITE_ARTICLES = 0x04
    MODERATE_COMMENTS = 0x08
    ADMINISTER = 0x80


class User(db.Model):
    __tablename__ = "auth_user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), unique=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('user_roles.id'))

    def __repr__(self):
        return '<User {}>'.format(self.username)


    def __init__(self, **kwargs):
        '''构造函数：首先调用基类构造函数，如果创建基类对象后没定义角色，则根据email地址决定其角色'''
        super(User, self).__init__(**kwargs)
        if self.role is None:
            # if self.email == current_app.config['FLASKY_ADMIN']:
            #     self.role = Role.query.filter_by(permissions=0xff).first()
            # if self.role is None:
            self.role = Role.query.filter_by(default=True).first()


# app/models.py

class Role(db.Model):
    __tablename__ = 'user_roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)  # 值是整数，表示位标志。
    users = db.relationship('auth_user', backref='role', lazy='dynamic')

    def __repr__(self):
        return "<Role {}>".format(self.name)


    @staticmethod
    def insert_roles():
        '''并不直接创建角色，而是根据数据库现有角色，然后进行更新。以后角色有更改也可执行同样操作。'''
        roles = {
            'User': (Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES, True),
            'Moderator': (
            Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARTICLES | Permission.MODERATE_COMMENTS,
            False),
            'Administrator': (0xff, False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()