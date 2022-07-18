from flask import Blueprint, render_template, redirect, url_for
from meine.models import Board, Posts, db
from meine.chan.forms import PostForm
from flask_login import current_user

chan_blueprint = Blueprint('chan', __name__, template_folder='templates')

@chan_blueprint.route('/')
def home():
    boards = Board.query.all()
    return render_template('chan/home.html', boards=boards)


@chan_blueprint.route('/board/<id>', methods=['POST', 'GET'])
def board(id):
    form = PostForm()
    board = Board.query.get(id)

    if form.validate_on_submit():
        if current_user.is_authenticated:
            user_id = current_user.id
            auth = current_user.name
            new_post = Posts(auth=auth, content=form.text.data, board_id=board.id, user_id=user_id)
        else:
            new_post = Posts(auth=form.name.data, content=form.text.data, board_id=board.id, user_id=None)
        # new_post = Posts(auth=form.name.data, content=form.text.data, board_id=board.id, user_id=user_id)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('chan.board', id=board.id))
    return render_template('chan/board.html', board=board, form=form)
