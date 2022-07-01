from flask import Blueprint, render_template, flash, redirect, url_for
from meine.users.forms import LoginForm
from meine.models import Users
from flask_login import login_user

users_blueprint = Blueprint('users', __name__, template_folder='templates')

@users_blueprint.route('/', methods=['POST', 'GET'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(name=form.name.data).first()
        if not user:
            flash('Nie ma takiego użytkownika')
        else:
            if user.check_password(form.password.data):
                login_user(user)
                return redirect(url_for('home'))
            else:
                flash('Złe hasło')



    return render_template('users/home.html', form=form)
