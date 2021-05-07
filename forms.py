from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired(message="Name cannot be blank")])

    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[InputRequired(message="Please pick a species")])

    photo_url = StringField("Photo URL", validators=[URL(), Optional()])

    age = IntegerField("How old is this pet?", validators=[NumberRange(min=0, max=30, message=f"Age must be between {min} - {max}")])

    notes = TextAreaField("Additonal notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", validators=[URL(), Optional()])

    notes = TextAreaField("Additional notes", validators=[Optional()])

    available = BooleanField("Available?", validators=[Optional()])
    