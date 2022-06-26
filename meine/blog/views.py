from flask import Blueprint, render_template
from meine.models import Board

blog_blueprint = Blueprint('blog', __name__, template_folder='templates')

@blog_blueprint.route('/')
def home():
    boards = Board.query.all()
    return render_template('blog/home.html', boards=boards)


@blog_blueprint.route('/board/<name>')
def board(name):
    return render_template('blog/board.html', name=name)
