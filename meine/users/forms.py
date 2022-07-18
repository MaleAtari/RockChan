from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, RadioField
from wtforms.validators import data_required, EqualTo
from meine.models import Board


def board_list():
    default = (0, 'Nic nie usuwaj')
    choice = [default]
    for board in Board.query.all():
        choice.append((board.id, board.name))

    return choice


class LoginForm(FlaskForm):

    name = StringField('Podaj Login', validators=[data_required()])
    password = PasswordField('Podaj Hasło', validators=[data_required()])
    submit = SubmitField('Potwierdz')

class AdminControlForm(FlaskForm):
    submit = SubmitField('Zapisz zmiany')

class BoardForm(FlaskForm):
    name = StringField('Nazwa Tablicy', validators=[data_required()])
    info = TextAreaField('Opis Tablicy')
    submit = SubmitField('Dodaj Tablicę')

class DelBoardForm(FlaskForm):
    menu = RadioField('Tablica do usunięcia')
    submit = SubmitField('Usuń !!!')

class DelPost(FlaskForm):
    submit = SubmitField('TAK')

class ChangePass(FlaskForm):
    old_pass = PasswordField('Podaj swoje stare hasło', validators=[data_required()])
    new_pass = PasswordField('Podaj nowe hasło', validators=[data_required()])
    confirm_pass = PasswordField('Powtórz nowe hasło', validators=[data_required(), EqualTo('new_pass', message='Pola z nowym hasłem muszą być takie same')])
    submit = SubmitField('ZMIEŃ')

