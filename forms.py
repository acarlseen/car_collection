'''
This is pretty boiler-plate code. Here's a rundown:
UserLoginForm class inherits attributes from FlaskForm class from flask_wtf, a subclass of wtforms

StringField is an object containing 
    .label (first parameter) to call in html later {{ in this format }}
    .validators is an iterable of methods applied to (checked against) the form input
        can be found in wtforms > validators

PasswordField is a special StringField that does not render input

SubmitField is a submit button
'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    email = StringField('Email', validators= [DataRequired(), Email()])
    password = PasswordField('Password', validators= [DataRequired()])
    submit_button = SubmitField()