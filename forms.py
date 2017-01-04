from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class NewMenuItem(Form):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description',  validators=[DataRequired()])
    price = StringField('Price',  validators=[DataRequired()])

class EditMenuItem(Form):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description',  validators=[DataRequired()])
    price = StringField('Price',  validators=[DataRequired()])
