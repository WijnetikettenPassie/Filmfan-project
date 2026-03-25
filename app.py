import sqlite3
def get_db():
    conn=sqlite3.connect("filmfan.db")
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON;")
    return conn

import os
from forms import LoginForm, RegistrationForm
from model import db,migrate
from flask import Flask, render_template,redirect,flash
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SECRET_KEY"] = "123"      #Acceptabel voor dit project maar normaal niet verstandig
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate.init_app(app,db)

#Homepage
@app.route("/")
def home():
    return render_template("filmfan1.html")

#Loginfunctionaliteit
@app.route("/login", methods= ["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        wachtwoord = form.wachtwoord.data
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM user WHERE email = ? AND password = ?",(email,wachtwoord))
        row = cursor.fetchone()
        db.close()
        if row is None:
            flash ('wachtwoord en email komen niet overeen','danger')
        else:
            flash ("login succesvol",'success')
        return redirect("/login")
    return render_template("login.html",form=form)

@app.route("/register", methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.wachtwoord.data
        geboortedatum = form.geboortedatum.data.strftime('%Y-%m-%d')  # Sla datum op als YYYY-MM-DD

        db = get_db()
        try:
            db.execute(
                "INSERT INTO user (username, email, password, geboortedatum) VALUES (?, ?, ?, ?)",
                (username, email, password, geboortedatum)
            )
            db.commit()
        except sqlite3.IntegrityError:
            # Als username of email al bestaat
            return "Gebruikersnaam of email bestaat al!"
        finally:
            db.close()

        return redirect("/")
    return render_template("registreren.html",form=form)
        



