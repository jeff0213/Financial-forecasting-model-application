# -*- coding: utf-8 -*-
# @Time    : 2022/1/27 10:38
# @Author  : jeff0213
# @File    : views.py
# @Software: PyCharm
import os

from flask import request, render_template, redirect, url_for, session

from flask import Blueprint
from flask.views import MethodView

import json

import test
from app import db
from mm.models import User,ModelUseLog

model = Blueprint('model', __name__)


# 根据图片文件路径获取hyp
def load_json(FilePath):
    with open(FilePath, 'r') as load_f:
        load_dict = json.load(load_f)
    return load_dict


def return_img_stream(img_local_path='static/assets/images/potato.jpg'):
    """
    工具函数:
    获取本地图片流
    :param img_local_path:文件单张图片的本地绝对路径
    :return: 图片流
    """
    import base64
    img_stream = ''
    with open(img_local_path, 'rb') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream).decode()
    return img_stream


# @model.route('/use/')
# def use():
#     return render_template('model/use-model.html')

class ModelView(MethodView):
    def get(self):
        if session.get('admin', None) is None:
            return redirect(url_for('login'))
        else:

            # user_name = request.args.get('username')
            # return render_template('model/use-model.html',username = user_name)
            img_stream = return_img_stream()
            return render_template("model/use-model.html", img_stream=img_stream)

    def post(self):
        if request.method == "POST":
            path = "file/" + session['admin'] + "/"
            if os.path.exists(path) == False:
                os.makedirs(path)
            # 获取上传文件数据
            file = request.files.get('files')
            # 保存文件到根目录
            file.save(path + file.filename)
            load_dict = load_json(path + file.filename)
            img_path = "user_result/" + session['admin'] + "/"
            if os.path.exists(img_path) == False:
                os.makedirs(img_path)
            result_path = test.patent_evaluation(load_dict, img_path)
            img_stream = return_img_stream(result_path)

            id = db.session.query(User.uid).filter(User.login_name == session['admin']).first()[0]

            ret = ModelUseLog(model_id=1, quantity=1, user_id=id)
            db.session.add(ret)
            db.session.commit()
            db.session.close()
            return render_template("model/use-model.html", img_stream=img_stream)
        else:
            return render_template("model/use-model.html")


model.add_url_rule('/use/', view_func=ModelView.as_view('use_model'))
