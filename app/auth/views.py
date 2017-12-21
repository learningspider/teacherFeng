#coding:utf-8
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user,login_required
from app import db
from app.auth import auth
from app.auth.forms import LoginForm
from app.models import User



print u'auth.route已启动'
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
       return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
    return render_template('auth/login.html',title=u'登录', form=form)
    # return render_template('auth/login.html')

@auth.route('/register')
def register():
    # flash('注册')
    return render_template('auth/register.html',title=u'注册')

@auth.route('/succees/')
@login_required
def login_success():
    return render_template('base.html')

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
