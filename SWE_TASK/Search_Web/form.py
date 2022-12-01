from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class SearchForm(Form):
    search_query = StringField('Search', validators=[DataRequired("Search for a book"), Length(max=50)])
    submit = SubmitField('search')
