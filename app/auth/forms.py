from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from ..models import Player



class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Second Name', validators=[DataRequired()])
    position = StringField('Field position', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired(),
                                EqualTo('confirm_password')])
    confirm_password = StringField('Confirm Password', validators=[DataRequired()])
    submit =SubmitField('Register')

    def validate_email(self, field):
        if Player.query.filter_by(email=field.data).first():
            raise ValidationError('Email already taken')

    def validate_username(self,field):
        if Player.query.filter_by(username=field.data).first():
            raise ValidationError('Username already taken')

            
class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')



