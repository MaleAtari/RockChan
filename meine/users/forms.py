from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import data_required


class LoginForm(FlaskForm):

    name = StringField('Podaj Login', validators=[data_required()])
    password = PasswordField('Podaj Hasło', validators=[data_required()])
    submit = SubmitField('Potwierdz')
