from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user, current_user


from .. import login_manager
from forms import SignUpForm, LoginForm
from models import User, db

authorization = Blueprint('authorization', __name__, 
                          template_folder='auth_templates', 
                          static_folder='static', 
                          static_url_path='/auth')

@authorization.route('/signin', methods=['GET', 'POST'])
def sign_in():
    if current_user.is_authenticated:
        return redirect(url_for('.home'))
    form = LoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data

            log_user = User.query.filter(User.email == email).first()
            if log_user and User.check_password(log_user.password, password):
                login_user(log_user)
                return redirect(url_for('site.collection'))
            else:
                flash('Username and/or password does not match')
    except:
        raise Exception('Incorrect form data, check form')
    return render_template('/sign_in.html', form=form)

@authorization.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data

            user = User(email, password=password)

            db.session.add(user)
            db.session.commit()

            flash(f'Thank you, account for {email} created')
            return redirect(url_for('site.home'))

    except:
        pass
    return render_template('sign_up.html', form=form)

@authorization.route('/signout')
def sign_out():
    logout_user()
    return redirect(url_for('site.home'))

@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)
    return None

@login_manager.unauthorized_handler
def unauthorized():
    flash('You must be logged in to view that page.')
    return redirect(url_for('authorization.sign_in'))