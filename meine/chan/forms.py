from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import data_required

class PostForm(FlaskForm):
    name = StringField('Podaj Nick', validators=[data_required()])
    text = TextAreaField('Napisz coś', validators=[data_required()])
    submit = SubmitField('Wyślij')
