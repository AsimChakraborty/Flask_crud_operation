from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flaskblog.models import User
# import email_validator

class RegistrationForm(FlaskForm):
   username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
   # email=StringField('Email',validators=[DataRequired(),Email()])
   password=PasswordField('Password',validators=[DataRequired()])
   confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
   submit=SubmitField('Sign Up')
   def validate_username(self,username):
      user=User.query.filter_by(username=username.data).first()
      if user:
         raise ValidationError('that username is taken')


class LoginForm(FlaskForm):
   username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
   # email=StringField('Email',validators=[DataRequired(),Email()])
   password=PasswordField('Password',validators=[DataRequired()])
  #  confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
   remember=BooleanField("Remember Me")
   submit=SubmitField('Login')   



class UpdateAccountForm(FlaskForm):
   username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
   picture=FileField('Update profile Picture',validators=[FileAllowed(['jpg','png'])])
   # email=StringField('Email',validators=[DataRequired(),Email()])
   # password=PasswordField('Password',validators=[DataRequired()])
   # confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
   submit=SubmitField('Update')
   def validate_username(self,username):
      if username.data != current_user.username:
         user=User.query.filter_by(username=username.data).first()
         if user:
            raise ValidationError('that username is taken')


class PostForm(FlaskForm):
   title =StringField('Title',validators=[DataRequired()])
   content=TextAreaField('Content',validators=[DataRequired()])
   submit =SubmitField('Post')
