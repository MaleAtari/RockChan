from meine import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from flask_bcrypt import Bcrypt


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)



bcrypt = Bcrypt()

class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(256))
    role = db.Column(db.Integer)
    date_add = db.Column(db.DateTime, nullable=False, default=datetime.now)
    date_log = db.Column(db.DateTime, nullable=False, default=datetime.now)
    posts = db.relationship('Posts', backref='user')

    def __init__(self, name, password):
        self.name = name
        self.password = bcrypt.generate_password_hash(password)
        self.role = 1


    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def show_date_add(self):
        return self.date_add.strftime("%D  %H:%M:%S")

    def show_date_log(self):
        return self.date_log.strftime("%D  %H:%M:%S")

    def set_password(self, new_password):
        self.password = bcrypt.generate_password_hash(new_password)





class Board(db.Model):
    __tablename__ = 'board'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    date_add = db.Column(db.DateTime, nullable=False, default=datetime.now)
    info = db.Column(db.Text)
    closed = db.Column(db.Boolean, default=False)
    posts = db.relationship('Posts', backref='boards')


    def show_date(self):
        return self.date_add.strftime("%D  %H:%M")

class Posts(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    date_add = db.Column(db.DateTime, nullable=False, default=datetime.now)
    date_edit = db.Column(db.DateTime)
    auth = db.Column(db.String(128))
    content = db.Column(db.Text)
    board_id = db.Column(db.ForeignKey(Board.id))
    user_id = db.Column(db.ForeignKey(Users.id))

    def show_date(self):
        # return self.date_add.strftime("%D  %H:%M:%S")
        return self.date_add.strftime("%D  %H:%M")

    def show_edit_date(self):
        return self.date_edit.strftime("%D  %H:%M")

    def set_edit_date(self):
        self.date_edit = datetime.now()

    def check_owner(self):
        if self.user_id:
            return True
        else:
            return False

