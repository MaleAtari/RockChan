from meine import app
from flask import render_template


@app.route('/')
def home():
    return render_template('home.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/access/denied')
def no_enter():
    return render_template('no_enter.html')