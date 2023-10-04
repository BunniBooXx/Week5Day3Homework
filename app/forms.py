from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    query= StringField(label='Search',validators=[DataRequired()])
    submit= SubmitField(label='Submit')

class LoginForm(FlaskForm): 
    query=StringField(label='Username', validators=[DataRequired()])
    query=StringField(label='Last Name', validators=[DataRequired()])
    query