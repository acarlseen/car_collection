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
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional

class SignUpForm(FlaskForm):
    email = StringField('Email', validators= [DataRequired(), Email(message='Enter a valid email')])
    password = PasswordField('Password', validators= [DataRequired(), Length(min=8, message='Select a stronger password')])
    confirm = PasswordField('Confirm your password', validators=[DataRequired(), EqualTo('password', message="Passwords do not match")])
    submit_button = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message='Enter a valid email')])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField('Log In')

class CarDesc(FlaskForm):
    make = StringField('Make', validators=[DataRequired(message='Vehicle make is required')])
    model = StringField('Model', validators=[DataRequired(message='Vehicle model is required')])
    year = IntegerField('Year', validators=[DataRequired(message='Vehiclke model year is required'), Length(min=4, max=4, message="Please enter a 4 digit year")])
    color = StringField('Color', validators=[Optional()])
    VIN = StringField('VIN', validators=[DataRequired(message='Please enter VIN')])
    car_name = StringField('Name your car (Optional)', validators=[Optional(), Length(max=60)])
    car_desc = TextAreaField('Describe your car/mods (Optional)', validators=[Optional(), Length(min=4, max=300)])
    submit_button = SubmitField('Add to collection')