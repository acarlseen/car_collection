from flask import Blueprint, render_template, request, redirect, url_for
from models import User, Car, db, check_password_hash

authorization = Blueprint('authorization', __name__, template_folder='/auth_templates')

@authorization.route('/signin')
def sign_in():
    pass

@authorization.route('/signup')
def sign_up():
    pass

@authorization.route('/signout')
def sign_out():
    pass