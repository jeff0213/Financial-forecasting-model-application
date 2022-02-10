# -*- coding: utf-8 -*-
# @Time    : 2022/1/26 14:52
# @Author  : jeff0213
# @File    : views.py
# @Software: PyCharm


from flask import Blueprint, render_template, session, redirect,url_for
from flask.views import MethodView

from app import *
from app import db
from .models import ModelUseLog

use = Blueprint("use", __name__)


class UseView(MethodView):
    def get(self):
        if session.get('admin',None) is None:
            return redirect(url_for('login'))
        else:
            # items = db.session.query(ModelUseLog).all()
            items = db.session.query(ModelUseLog.model_id,ModelUseLog.user_id, db.func.count(ModelUseLog.user_id).label('quantity')).group_by("user_id","model_id")
            return render_template('admin/user-list.html', items=items)

use.add_url_rule('/list/', view_func=UseView.as_view('use_list'))


