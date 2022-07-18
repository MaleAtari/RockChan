from flask import Blueprint, render_template, flash, redirect, url_for, request, flash
from meine.users.forms import LoginForm, BoardForm, DelPost, ChangePass
from meine.models import Users, Board, db, Posts
from flask_login import login_user, login_required, logout_user, current_user

users_blueprint = Blueprint('users', __name__, template_folder='templates')

def edit_comment(post, new_content):
    if post.date_edit == None:
        post.edit_date = post.set_edit_date()
        db.session.add(post)
        db.session.commit()

    signature = f"\n\n\nPost edytowany: {post.show_edit_date()} przez {current_user.name}"
    post.content = str(new_content) + str(signature)
    db.session.add(post)
    db.session.commit()

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


@users_blueprint.route('/edit/<id>', methods=['POST', 'GET'])
@login_required
def edit_post(id):
    edited = Posts.query.get(id)
    if request.method == 'POST':
        new = request.form['editedPost']
        edit_comment(edited, new)

        return redirect(url_for('blog.board', id=edited.board_id))



    return render_template('users/edit_post.html', edited=edited)

@users_blueprint.route('/del/<id>', methods=['POST', 'GET'])
@login_required
def del_post(id):
    deleted = Posts.query.get(id)
    del_post = DelPost()
    if del_post.validate_on_submit():
        db.session.delete(deleted)
        db.session.commit()
        return redirect(url_for('blog.board', id=deleted.board_id))
    return render_template('users/del_post.html', deleted=deleted, form=del_post)

@users_blueprint.route('admin/account', methods=['POST', 'GET'])
@login_required
def change_pass():
    form = ChangePass()
    c_user = Users.query.get(current_user.id)

    if form.validate_on_submit():
        if not c_user.check_password(form.old_pass.data):
            flash('Stare hasło jest niepoprawne')
        else:

            print(form.confirm_pass.errors)
            c_user.set_password(form.confirm_pass.data)
            db.session.add(c_user)
            db.session.commit()
            flash('Ustawiono nowe hasło')


    return render_template('users/change_pass.html', form=form)
