from wtforms import Form, StringField, TextAreaField, IntegerField, DateTimeField, FloatField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField

class MovieForm(Form):
    title = StringField('Title')
    description = TextAreaField('Description')
    tagline = TextAreaField('Tagline')
    fees_in_world = FloatField('Fees in world')
    budget = FloatField('Budget')
    country = StringField('Country')
    premiere = DateTimeField('Premiere')
    year = IntegerField('Year')

class UploadForm(FlaskForm):
    file = FileField()
