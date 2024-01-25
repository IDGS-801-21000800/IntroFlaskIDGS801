from wtforms import Form
from wtforms import StringField, TelField

class UseForm(Form):
    nombre=StringField("nombre")
    email=StringField("email")