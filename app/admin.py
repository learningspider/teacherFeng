#coding:utf-8
from flask_admin import Admin,BaseView,expose
from flask_admin.contrib.sqla import ModelView
from flask_login import login_required

admin = Admin(name=u'博成教育后台系统')



class MyView(BaseView):
    @expose('/')
    @login_required
    def index(self):
        return self.render('admin/index.html')

    @expose('/abc')
    def abc(self):
        return self.render('admin/abc.html')

admin.add_view(MyView(name=u'网站基本设置'))



from app import db
from models import Role,User,SpendList,Recharge,Subject,Belond,Lesson,Plan,Video,MenuList,IndexContent
class myModelView(ModelView):
    pass

models = [Role,User,SpendList,Recharge,Subject,Belond,Lesson,Plan,Video,MenuList,IndexContent]
for model in models:
    admin.add_view(myModelView(model,db.session, category=u'数据库基本设置'))
