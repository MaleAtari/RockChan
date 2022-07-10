from flask import Blueprint, render_template, flash, redirect, url_for, request
from meine.users.forms import LoginForm, BoardForm, DelBoardForm
from meine.models import Users, Board, db
from flask_login import login_user, login_required, logout_user, current_user

users_blueprint = Blueprint('users', __name__, template_folder='templates')

def board_list():
    default = (0, 'Nic nie usuwaj')
    choice = [default]
    for board in Board.query.all():
        choice.append((board.id, board.name))

    return choice

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

@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@users_blueprint.route('/admin')
@login_required
def admin():
    if current_user.role > 1:
        return redirect(url_for('home'))

    return render_template('users/admin.html')

@users_blueprint.route('/admin/board', methods=['POST', 'GET'])
@login_required
def add_board():
    form = BoardForm()
    if form.validate_on_submit():
        new_board = Board(name=form.name.data, info=form.info.data)
        db.session.add(new_board)
        db.session.commit()

        return redirect(url_for('blog.home'))

    return render_template('users/add_board.html', form=form)

@users_blueprint.route('/admin/delete', methods=['POST', 'GET'])
@login_required
def del_board():
    boards = Board.query.all()

    if request.method == 'POST':
        deleted = Board.query.get(request.form['boardRadio'])
        db.session.delete(deleted)
        db.session.commit()

        return redirect(url_for('users.del_board'))



    return render_template('users/del_board.html', boards=boards)

