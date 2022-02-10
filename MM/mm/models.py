# coding: utf-8
from datetime import datetime

from app import db


class Model(db.Model):
    """
    模型表
    """
    __tablename__ = 'model'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.BigInteger, nullable=False, index=True, info='uid')
    name = db.Column(db.String(255), nullable=False)

    def __init__(self, uid, name):
        self.uid = uid
        self.name = name
    #
    # def __repr__(self):
    #     return


class ModelUseLog(db.Model):
    __tablename__ = 'model_use_log'

    id = db.Column(db.Integer, primary_key=True)
    model_id = db.Column(db.Integer, nullable=False, index=True)
    quantity = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)


    def __int__(self, model_id, quantity, user_id, created_time):
        self.model_id = model_id
        self.quantity = quantity
        self.user_id = user_id

    # def __repr__(self):
    #     return '<模型 {} {} {}>'.format(self.model_id,self.user_id,self.quantity)

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.BigInteger, nullable=False, index=True, info='uid')
    login_name = db.Column(db.String(20), nullable=False, unique=True)
    login_pwd = db.Column(db.String(32), nullable=False)
    status = db.Column(db.Integer, nullable=False)



    def __int__(self, uid, login_name, login_pwd, status, updated_time, created_time):
        self.uid = uid
        self.login_name = login_name
        self.login_pwd = login_pwd
        self.status = status
