from flask import Blueprint, render_template, redirect, url_for
from meine.models import Board, Posts, db
from meine.blog.forms import PostForm

blog_blueprint = Blueprint('blog', __name__, template_folder='templates')

@blog_blueprint.route('/')
def home():
    boards = Board.query.all()
    return render_template('blog/home.html', boards=boards)


@blog_blueprint.route('/board/<id>', methods=['POST', 'GET'])
def board(id):
    form = PostForm()
    board = Board.query.get(id)
    if form.validate_on_submit():
        new_post = Posts(auth=form.name.data, content=form.text.data, board_id=board.id)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('blog.board', id=board.id))
    return render_template('blog/board.html', board=board, form=form)
