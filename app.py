from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import AddPetForm

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///pet_adoption_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config["SECRET_KEY"] = "mango-pudding"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def homepage():

    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add_pet():

    form = AddPetForm()
    if form.validators_on_submit():
      
