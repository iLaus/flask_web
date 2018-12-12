# -*- coding: utf-8 -*-
#!/usr/bin/python

from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_utils import ChoiceType


class Role(db.Model):
    ROLE_ADMINISTER = "administer"
    ROLE_OPERATE = "operate"
    ROLE_STAFF = "staff"
    ROLE_USER = "user"
    ROLE_CHOICE = (
        (ROLE_ADMINISTER, u"管理员"),
        (ROLE_OPERATE, u"运营"),
        (ROLE_STAFF, u"内部职员"),
        (ROLE_USER, u"用户"),
    )

    __tablename__ = 'user_roles'

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    role_name = db.Column(db.String(20))
    # role = db.Column(ChoiceType(ROLE_CHOICE))
    users = db.relationship('User', backref='role_i')
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=None, onupdate=datetime.now)

    def __repr__(self):
        return "<Role {}>".format(self.name)


    @staticmethod
    def insert_roles():
        '''创建角色'''

        for r in Role.ROLE_CHOICE:
            role = Role.query.filter_by(name=r[1]).first()
            if role is None:
                role = Role(name=r[1])
            role.role_name = r[0]
            if r[0] == Role.ROLE_USER:
                role.default = True
            else:
                role.default = False

            print("insert user role: {}".format(role))

            db.session.add(role)
        db.session.commit()


class User(db.Model):
    __tablename__ = "auth_user"
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=True)

    Shadow = db.Column(db.String(200), unique=True, nullable=False)
    # password = db.Column(db.String(128), unique=True, nullable=False)
    # role_id = db.Column(db.Integer, db.ForeignKey('Role.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('user_roles.id'))
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=None, onupdate=datetime.now)

    def __repr__(self):
        return '<User {}>'.format(self.username)


    #将password字段定义为User类的一个属性，其中设置该属性不可读，若读取抛出AttributeError。
    @property
    def password(self):
        raise AttributeError('password cannot be read')

    #定义password字段的写方法，我们调用generate_password_hash将明文密码password转成密文Shadow
    @password.setter
    def password(self, password):
        self.Shadow = generate_password_hash(password)

    #定义验证密码的函数confirm_password
    def confirm_password(self, password):
        return check_password_hash(self.Shadow, password)



    def __init__(self, **kwargs):
        '''构造函数：首先调用基类构造函数，如果创建基类对象后没定义角色，则根据email地址决定其角色'''
        super(User, self).__init__(**kwargs)
        if self.role_id is None:
            # if self.email == current_app.config['FLASKY_ADMIN']:
            #     self.role = Role.query.filter_by(permissions=0xff).first()
            # if self.role is None:
            self.role_id = Role.query.filter_by(default=True).first().id

