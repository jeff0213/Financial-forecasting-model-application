# -*- coding: utf-8 -*-
# @Time    : 2022/2/10 9:54
# @Author  : jeff0213
# @File    : views.py
# @Software: PyCharm
import os

from flask import request, render_template, redirect, url_for, session

from flask import Blueprint
from flask.views import MethodView

import json

import interface_test
from app import db
from mm.models import User, ModelUseLog

interface = Blueprint('zlsq', __name__)


class ZlsqView(MethodView):
    def get(self):
        if request.args['username'] and request.args['pwd']:
            return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
            u = request.args['username']
            p = request.args['pwd']
            user = db.session.query(User.uid).filter(User.login_name == u, User.login_pwd == p).first()[0]
            if user != '':
                return json.dumps(return_dict, ensure_ascii=False)

    def post(self):
        if request.args['username'] and request.args['pwd']:

            u = request.args['username']
            p = request.args['pwd']
            user = db.session.query(User.uid).filter(User.login_name == u, User.login_pwd == p).first()[0]
            if user != '':
                return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
                # 判断传入的json数据是否为空
                if request.get_data() == b'':
                    return_dict['return_code'] = '5004'
                    return_dict['return_info'] = '请求参数为空'
                    return json.dumps(return_dict, ensure_ascii=False)
                # 获取传入的参数
                get_Data = request.get_data()
                # 传入的参数为bytes类型，需要转化成json
                get_Data = json.loads(get_Data)

                # 判断参数是否缺失
                hyp_list_base = ['Fin_BusinessTurnover', 'Fin_Direct_costs', 'Fin_Indirect_costs',
                                 'Fin_ProvisionForDeprec', 'Fin_DeprecPeriod', 'Def_of_BusinessArea',
                                 'Fin_DiscountFactor', 'Fin_TotalGrowthIn_General_CompanyMarket', 'B5', 'C2', 'C3',
                                 'C6', 'D1', 'D2', 'D3', 'D4']

                for item in hyp_list_base:
                    if get_Data.get(item) is None:
                        return_dict['return_code'] = '5004'
                        return_dict['return_info'] = item+'参数为空'
                        return json.dumps(return_dict, ensure_ascii=False)

                img_path = "user_result/" + u + "/"
                if os.path.exists(img_path) == False:
                    os.makedirs(img_path)

                result = interface_test.patent_evaluation(get_Data, img_path)

                id = db.session.query(User.uid).filter(User.login_name == u).first()[0]

                ret = ModelUseLog(model_id=1, quantity=1, user_id=id)
                db.session.add(ret)
                db.session.commit()
                db.session.close()

                return_dict['result'] = result
                return json.dumps(return_dict, ensure_ascii=False)


interface.add_url_rule('/zlsq/', view_func=ZlsqView.as_view('zlsq_model'))
