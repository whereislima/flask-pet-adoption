from flask_sqlalchemy import SQLAlchemy

DEFAULT_PROFILE_PIC = "https://bit.ly/2SzcQdB"

db = SQLAlchemy()

class Pet(db.Model):
    """ Pet """
    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    species = db.Column(db.Text,
                     nullable=False)
    photo_url = db.Column(db.Text, default=DEFAULT_PROFILE_PIC)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, default=True)
    
def connect_db(app):
    db.app = app
    db.init_app(app)