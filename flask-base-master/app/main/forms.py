from flask import url_for
from flask_wtf import FlaskForm
from wtforms import ValidationError
from wtforms.fields import (
    BooleanField,
    PasswordField,
    StringField,
    SubmitField,
    FieldList
)
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, EqualTo, InputRequired, Length

from app.models import User, Courses

from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
  search = StringField('search', [DataRequired()])
  submit = SubmitField('Search',
                       render_kw={'class': 'btn btn-success btn-block'})
                           
