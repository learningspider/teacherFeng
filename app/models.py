#coding:utf-8
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from app import db

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Permission:
    NormalUser = 1
    ADMIN = 2

class Role(db.Model):
    __tablename__ = 'tb_Roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

class User(UserMixin, db.Model):
    __tablename__ = 'tb_Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('tb_Roles.id'))
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

# #系统权限表
# class Role(db.Model):
#     __tablename__ = 'tb_Roles'
#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(64),unique=True)
#     users = db.relationship('User',backref='role')
#
#     def __repr__(self):
#         return '<Role %r>' % self.name
#
# #用户表
# class User(UserMixin,db.Model):
#     __tablename__ = 'tb_Users'
#     id = db.Column(db.Integer,primary_key = True,index=True)
#     UserName = db.Column(db.String(12),unique=True)
#     Sex = db.Column(db.Boolean)
#     Password_hash = db.Column(db.String(128))
#     Level = db.Column(db.Integer)
#     Truename = db.Column(db.String(64))
#     Email = db.Column(db.String(64),unique=True)
#     PhoneCode = db.Column(db.String(16),unique=True)
#     City = db.Column(db.String(64))
#     Address = db.Column(db.String(64))
#     PostCode = db.Column(db.String(8))
#     LastDate = db.Column(db.DateTime)
#     RedDate = db.Column(db.DateTime)
#     Point = db.Column(db.Integer)
#
#     role_id = db.Column(db.Integer,db.ForeignKey('tb_Roles.id'))
#     order_id = db.relationship('SpendList',backref='user')
#     user_id = db.relationship('Recharge',backref='user')
#
#
#     @property
#     def password(self):
#         raise AttributeError('password is not a readable attribute')
#     @password.setter
#     def password(self,password):
#         self.password_hash = generate_password_hash(password)
#     def verify_password(self,password):
#         return check_password_hash(self.password_hash,password)
#
#     def __repr__(self):
#         return '<User %r>' % self.UserName
#
# #消费订单表
# class SpendList(db.Model):
#     __tablename__ = 'tb_SpendList'
#     OrderID = db.Column(db.Integer,primary_key=True,index=True)
#     UserID = db.Column(db.Integer,db.ForeignKey('tb_Users.id'))
#     PricePoint = db.Column(db.Integer)
#     TotalPoint = db.Column(db.Integer)
#     OrderTime = db.Column(db.DateTime)
#     LessonID = db.Column(db.Integer,db.ForeignKey('tb_Lesson.LID'))
#     IsConfirm = db.Column(db.Boolean)
#     IsPayment = db.Column(db.Boolean)
#     LID = db.relationship('Lesson',backref='SpendList',foreign_keys=[LessonID])
#
#     def __repr__(self):
#         return '<SpendList %r>' % self.OrderID
#
# #充值表
# class Recharge(db.Model):
#     __tablename__ = 'tb_Recharge'
#     id = db.Column(db.Integer,primary_key=True)
#     UserID = db.Column(db.Integer,db.ForeignKey('tb_Users.id'))
#     RechPoint = db.Column(db.Integer)
#     RechTime = db.Column(db.DateTime)
#     RechChannel = db.Column(db.String(20))
#
#     def __repr__(self):
#         return '<Recharge %r>' % self.id
#
# #科目类别表
# class Subject(db.Model):
#     __tablename__ = 'tb_Subject'
#     SID = db.Column(db.Integer,primary_key=True)
#     Sname = db.Column(db.String(30))
#
#     def __repr__(self):
#         return '<Subject %r>' % self.SID
#
# #课程从属类别表
# class Belond(db.Model):
#     __tablename__ = 'tb_Belond'
#     BID = db.Column(db.Integer,primary_key=True)
#     LID = db.relationship('Lesson',backref='belond')
#     BelondTo = db.Column(db.Integer)
#
#
#     def __repr__(self):
#         return '<Belond %r>' % self.BID
#
# #课程详细内容表
# class Lesson(db.Model):
#     __tablename__ = 'tb_Lesson'
#     LID = db.Column(db.Integer,primary_key=True)
#     Lname = db.Column(db.String(30))
#     Publisher = db.Column(db.String(12))
#     ReleaseTime = db.Column(db.DateTime)
#     PayPoint = db.Column(db.Integer)
#     StudyCount = db.Column(db.Integer)
#     BelondPlanID = db.Column(db.Integer)
#     VLD = db.Column(db.String(30))
#     Introduce = db.Column(db.String(255))
#     Teacher = db.Column(db.String(12))
#     LastDatetime = db.Column(db.DateTime)
#     DemoVideo = db.Column(db.Integer)
#     ViewImageUrl = db.Column(db.String(255))
#
#     OrderID = db.Column(db.Integer,db.ForeignKey('tb_SpendList.OrderID'))
#     BID = db.Column(db.Integer,db.ForeignKey('tb_Belond.BID'))
#
#     def __repr__(self):
#         return '<Lesson %r>' % self.LID
#
# #教学计划表
# class Plan(db.Model):
#     __tablename__ = 'tb_Plan'
#     PlanID = db.Column(db.Integer,primary_key=True)
#     PlanName = db.Column(db.String(30))
#     PlanContent = db.Column(db.String(255))
#
#     def __repr__(self):
#         return '<Plan %r>' % self.PlanID
#
# #视频内容表
# class Video(db.Model):
#     __tablename__ = 'tb_Video'
#     VideoID = db.Column(db.Integer,primary_key=True)
#     VideoName = db.Column(db.String(30))
#     VideoUrl = db.Column(db.String(255))
#
#     def __repr__(self):
#         return '<Video %r>' % self.VideoID
#
# #课程目录内容表
# class MenuList(db.Model):
#     __tablename__ = 'tb_MenuList'
#     MID = db.Column(db.Integer,primary_key=True)
#     ChapterID = db.Column(db.Integer)
#     Mname = db.Column(db.String(32))
#     VideoID = db.Column(db.Integer)
#
#     def __repr__(self):
#         return '<MenuList %r>' % self.MID
#
# #首页内容表
# class IndexContent(db.Model):
#     __tablename__ = 'tb_IndexContent'
#     id = db.Column(db.Integer,primary_key=True)
#     LogoUrl = db.Column(db.String(255))
#     BannerUrl = db.Column(db.String(255))
#     QRCodeUrl = db.Column(db.String(255))
#     KefuQQ = db.Column(db.String(12))
#     KefuQQun = db.Column(db.String(12))
#     Notice = db.Column(db.String(255))
#
#     def __repr__(self):
#         return '<IndexContent %r>' % self.id
