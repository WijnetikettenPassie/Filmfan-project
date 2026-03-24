import sqlite3
def get_db():
    conn=sqlite3.connect("filmfan.db")
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON;")
    return conn

import os
from model import db
from flask import Flask, render_template,redirect,flash
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,EqualTo
from wtforms import EmailField, PasswordField, StringField, SubmitField, DateField
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SECRET_KEY"] = "123"      #Acceptabel voor dit project maar normaal niet verstandig
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

#Homepage
@app.route("/")
def home():
    return render_template("filmfan1.html")

#Loginformulier velden naar forms.py
class LoginForm(FlaskForm):
    email = EmailField(validators=[DataRequired()],render_kw={"placeholder":"Email"})
    wachtwoord = PasswordField(validators =[DataRequired()],render_kw={"placeholder":"Wachtwoord"})
    submit = SubmitField("Inloggen",render_kw={"class": "btn login-button"})

class RegistrationForm(FlaskForm):
    username = StringField(validators=[DataRequired()],render_kw={"placeholder":"Gebruikersnaam"})
    email = EmailField(validators=[DataRequired()],render_kw={"placeholder":"Email"})
    wachtwoord = PasswordField(validators =[DataRequired()],render_kw={"placeholder":"Wachtwoord"})
    wachtwoordherhalen = PasswordField(validators = [DataRequired(),EqualTo("wachtwoord", message="Wachtwoorden komen niet overeen")],render_kw = {"placeholder":"Wachtwoord herhalen"})
    geboortedatum = DateField(validators = [DataRequired()],render_kw={"placeholder":"Dy/Mth/Year"})
    submit = SubmitField("Registreren",render_kw={"class": "btn login-button"})

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
        

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)






