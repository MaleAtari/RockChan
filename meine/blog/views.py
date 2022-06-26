from flask import Blueprint, render_template

blog_blueprint = Blueprint('blog', __name__, template_folder='templates')

@blog_blueprint.route('/')
def home():
    return render_template('blog/home.html')


@blog_blueprint.route('/board/<name>')
def board(name):
    return render_template('blog/board.html', name=name)
