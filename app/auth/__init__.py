#coding:utf-8
from flask import Blueprint

auth = Blueprint('auth',__name__)
print u'auth.init 已启动'
from app.auth import views
