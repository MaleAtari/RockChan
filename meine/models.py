from meine import db
from datetime import datetime


class Board(db.Model):
    __tablename__ = 'board'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    date_add = db.Column(db.DateTime, nullable=False, default=datetime.now)
    info = db.Column(db.Text)
    posts = db.relationship('Posts', backref='boards')

class Posts(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    date_add = db.Column(db.DateTime, nullable=False, default=datetime.now)
    auth = db.Column(db.String(128))
    content = db.Column(db.Text)
    board_id = db.Column(db.ForeignKey(Board.id))

    def show_date(self):
        return self.date_add.strftime("%D  %H:%M:%S")