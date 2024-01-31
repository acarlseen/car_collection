from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user


from .. import login_manager
from forms import SignUpForm, LoginForm
from models import User, db, check_password_hash

authorization = Blueprint('authorization', __name__, 
                          template_folder='auth_templates', 
                          static_folder='static', 
                          static_url_path='/auth')

@authorization.route('/signin', methods=['GET', 'POST'])
def sign_in():
    if current_user.is_authenticated:
        return redirect(url_for('site.home'))
    form = LoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data

            log_user = User.query.filter(User.email == email).first()
            print(type(log_user))
            if log_user and check_password_hash(log_user.password, password):
                login_user(log_user)
                return redirect(url_for('site.home'))
            else:
                flash('Username and/or password does not match')
    except:
        print(form.validate())
        print(form.errors)
        raise Exception('Incorrect form data, check form')
    return render_template('/sign_in.html', form=form)

@authorization.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('site.home'))
    
    form = SignUpForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email, password)

            user = User(email, password=password)

            db.session.add(user)
            db.session.commit()

            flash(f'Thank you, account for {email} created')
            return redirect(url_for('site.home'))
        elif form.validate_on_submit():
            print('form submitted successfully, some other problem')
        elif not form.validate_on_submit():
            print('The form is not valid')
            print(form.validate())
            print(form.errors)

    except:
        print('Something went horribly wrong')
        print(form.errors)
        raise Exception('User not added to database')
    return render_template('sign_up.html', 
                           title = 'Sign Up',
                           form=form)

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