#coding:utf-8
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user,login_required
from app import db
from app.auth import auth
from app.auth.forms import LoginForm,RegistrationForm
from app.models import User



print u'auth.route已启动'
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password')
    return render_template('auth/login.html',title=u'登录', form=form)

@auth.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print 1
        user = User(username=form.user.data,password=form.password.data)
        db.session.add(user)
        flash('login succees')
        return redirect(url_for(auth.login))
    return render_template('auth/register.html',title=u'注册',form=form)

@auth.route('/success/')
@login_required
def login_success():
    return render_template('base.html')

@auth.route('/logout')
def logout():
    logout_user()
    flash(u'您已退出登录')
    return redirect(url_for('main.index'))
