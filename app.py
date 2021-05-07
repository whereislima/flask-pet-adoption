from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import AddPetForm

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///pet_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config["SECRET_KEY"] = "mango-pudding"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def homepage():

    pets = Pet.query.all()

    return render_template("home.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():

    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
    
        return redirect("/")
    else:
        return render_template("add.html")
