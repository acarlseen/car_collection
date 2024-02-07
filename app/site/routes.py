from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required
from models import User

site = Blueprint('site', __name__, template_folder='site_temps', static_folder='static', static_url_path='/site')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/collection')
@login_required
def collection():
    return render_template('collection.html')

@site.route('/profile/<user_id>')
@login_required
def profile(user_id):
    user = User.query.filter_by(id = user_id).first()
    return render_template('profile.html',
                           user=user)

