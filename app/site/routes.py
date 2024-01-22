from flask import Blueprint, render_template
from flask_login import login_required

site = Blueprint('site', __name__, template_folder='site_temps', static_folder='static', static_url_path='/site')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/collection')
@login_required
def collection():
    return render_template('collection.html')