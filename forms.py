from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,PasswordField
from wtforms.validators import DataRequired,Length,Email,EqualTo
class Predict(FlaskForm):
    username=StringField('Username',
                         validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password =PasswordField('Password',
                        validators=[DataRequired()])
    confirm_password = PasswordField('Confirm_Password',
                           validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')
