#coding:utf-8
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Length,Regexp,DataRequired,EqualTo

class LoginForm(FlaskForm):
    # email = StringField('Email',validators=[DataRequired(),Length(1,64),Email()])
    username = StringField(u'用户名',validators=[Required(),Length(1,12)])
    password = PasswordField(u'密码',validators=[DataRequired()])
    remember_me = BooleanField(u'保持登录状态')
    submit = SubmitField(u'登录')


class RegistrationForm(FlaskForm):
    username = StringField(u'用户名',validators=[DataRequired(),Length(1,12),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,u'用户名只能由字母数字下划线组成')])
    password = PasswordField(u'密码',validators=[Required(),EqualTo('password2',message='password must match.')])
    password2 = PasswordField(u'再次输入密码',validators=[Required()])
    submit = SubmitField(u'注册')

def validate_username(self,field):
    if User.query.filter_by(username=field.data).first():
        raise ValidationError(u'用户名已存在')
