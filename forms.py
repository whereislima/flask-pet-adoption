from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, URLField
from wtforms.validators import InputRequired, Optional, url, NumberRange

class AddPetForm(FlaskForm):
  name = StringField("Pet Name", validators=[InputRequired(message="Name cannot be blank")])

  species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[InputRequired(message="Please pick a species")])

  photo_url = URLField("Photo URL", validators=[url(), Optional()])

  age = IntegerField("How old is this pet?", validators=[NumberRange(min=0, max=30, message=f"Age must be between {min} - {max}")])

  notes = StringField("Additional notes", validators=[Optional()])