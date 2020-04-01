from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(Form):
    search = StringField('', [DataRequired()])
    submit = SubmitField('Search', render_kw={"class": "btn btn-success btn-block"})

    