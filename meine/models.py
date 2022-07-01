from meine import db, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)





class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(256))
    role = db.Column(db.Integer)
    date_add = db.Column(db.DateTime, nullable=False, default=datetime.now)
    date_log = db.Column(db.DateTime, nullable=False, default=datetime.now)


    def check_password(self, password):
        if self.password == password:
            return True
        else:
            return False

    def show_date_add(self):
        return self.date_add.strftime("%D  %H:%M:%S")

    def show_date_log(self):
        return self.date_log.strftime("%D  %H:%M:%S")



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