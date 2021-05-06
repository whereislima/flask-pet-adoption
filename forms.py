from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, URLField, SelectField
from wtforms.validators import InputRequired, Email, Optional, url, NumberRange

class AddPetForm(FlaskForm):
  name = StringField("Pet Name", validators=[InputRequired(message="Name cannot be blank")])

  species = SelectField("Species", choices=[('cat', 'cat'), ('dog', 'dog'), ('porcupine', 'porcupine')], validators=[InputRequired(message="Please pick a species")])

  photo_url = URLField(validators=[url()], validators=[Optional(), NumberRange(min=0, max=30, message=f"Age must be between {min} - {max}")])

  age = IntegerField("How old is this pet?", validators=[Optional()])

  notes = StringField("Additional notes", validators=[Optional()])