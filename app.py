import sqlite3
import os
from forms import LoginForm, RegistrationForm
from model import db,migrate,User
from flask import Flask, render_template,redirect,flash,session
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
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(
            email=form.email.data,
            wachtwoord=form.wachtwoord.data
        ).first()

        if user is None:
            flash("Email of wachtwoord klopt niet", "danger")
        else:
            session["user_id"] = user.id
            session["username"] = user.username  
            flash("Login succesvol!", "success")
            return redirect("/")

    return render_template("login.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            wachtwoord=form.wachtwoord.data,
            geboortedatum=form.geboortedatum.data.strftime('%Y-%m-%d')
        )

        db.session.add(user)

        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            flash("Gebruikersnaam of email bestaat al!", "danger")
            return render_template("registreren.html", form=form)

        flash("Registratie succesvol!", "success")
        return redirect("/login")

    return render_template("registreren.html", form=form)

@app.route("/myaccount")
def myaccount():
    if not session.get("user_id"):
        flash("Je moet eerst inloggen om je account te zien.", "warning")
        return redirect("/login")
    else:
        return render_template("myaccount.html")


@app.route("/logout", methods = ["GET","POST"])
def logout():
    session.clear()
    return redirect("/")
