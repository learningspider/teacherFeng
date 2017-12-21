from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Length,Email,DataRequired

class LoginForm(FlaskForm):
    # email = StringField('Email',validators=[DataRequired(),Length(1,64),Email()])
    username = StringField('Username',validators=[DataRequired(),Length(1,12),[DataRequired()]])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
