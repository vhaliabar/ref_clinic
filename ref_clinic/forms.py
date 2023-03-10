""" forms - the mechanism to control user input behaviour """
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, EmailField
from wtforms.validators import DataRequired, Email, NumberRange

# Create a search form
class SearchForm(FlaskForm):
    """ form to be user in search func """
    searched = StringField('Searched',validators=[DataRequired()])
    submit = SubmitField('search')

# Create a form class
class DoctorForm(FlaskForm):
    """ form to be user in create_doctor func """
    email= EmailField('Email', validators=[Email()])
    years_xp= IntegerField('Years of experience',
                           validators=[DataRequired(), NumberRange(min=1,max=49)])
    name= StringField('Name')
    specialization= StringField('Doctor specialization',
                                validators=[DataRequired()])
    submit = SubmitField('Add doctor')
    