#coding=utf-8
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Length,Email

class LoginForm(FlaskForm):
    email = StringField('Email',validators = [Required(),Length(1,64),Email()])
    password = PasswordField('Password',validators=[Required()])
    remember_me = BooleanField(u'记住密码')
    submit = SubmitField(u'登陆')


class RegForm(FlaskForm):
    email = StringField('Email',validators = [Required(),Length(1,64),Email()])
    user = StringField('User',validators = [Required(),Length(4,64)])
    password = PasswordField('Password',validators=[Required()])
    phone = StringField('Phone',validators=[Required(),Length(11)])
