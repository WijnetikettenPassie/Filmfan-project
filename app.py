#TO DO:
    #Login en logoot functionality fixen
    #Blue prints inzetten
    #Searchbar maken
    #Database revisen
    #Hyperlinks stylen

import os
from sqlalchemy import text
from forms import LoginForm, RegistrationForm
from model import db,migrate,User,Film,Rol,Acteur,Regisseur,Favorite
from flask import Flask, render_template,redirect,flash,request,session,url_for
#from werkzeug.security import generate_password_hash, check_password_hash
#from flask_login import UserMixin , login_user, logout_user, login_required
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SECRET_KEY"] = "123"      #Acceptabel voor dit project maar normaal niet verstandig
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate.init_app(app,db)

# Homepage
@app.route("/")
def home():
    return render_template("home.html")

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        query = db.select(User).filter_by(email=form.email.data)
        user = db.session.execute(query).scalar_one_or_none()

        if user is None or not user.check_wachtwoord(form.wachtwoord.data):
            flash("Email of wachtwoord klopt niet", "danger")
            return render_template("login.html", form=form)

        session["user_id"] = user.id
        session["username"] = user.username
        flash("Login succesvol!", "success")
        return redirect("/")

    return render_template("login.html", form=form)

#logout
@app.route("/logout", methods = ["GET","POST"])
def logout():
    session.clear()
    return redirect("/")

# Registreren
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():

        geboortedatum = form.geboortedatum.data 

        user = User(
            username=form.username.data,
            email=form.email.data,
            wachtwoord="",
            geboortedatum=geboortedatum
        )
        user.set_wachtwoord(form.wachtwoord.data)

        db.session.add(user)

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)
            flash("Er ging iets mis bij het opslaan!", "danger")
            return render_template("registreren.html", form=form)

        flash("Registratie succesvol!", "success")
        return redirect("/login")

    return render_template("registreren.html", form=form)


# My Account
@app.route("/myaccount")
def myaccount():
    user_id = session.get("user_id")

    if not user_id:
        flash("Je moet eerst inloggen om je account te zien.", "warning")
        return redirect("/login")

    query = db.select(Favorite).filter_by(user_id=user_id)
    favorites = db.session.execute(query).scalars().all()

    return render_template("myaccount.html", favorites=favorites)


# Film pagina
@app.route("/film/<int:film_id>")
def film_pagina(film_id):
    film = Film.query.get_or_404(film_id)

    regisseur = Regisseur.query.get(film.regisseur_id)

    rollen = Rol.query.filter_by(film_id=film_id).all()

    # acteurs koppelen aan rollen
    rollen_met_acteurs = []
    for rol in rollen:
        acteur = Acteur.query.get(rol.acteur_id)
        rollen_met_acteurs.append({
            "personage": rol.personage,
            "acteur": acteur
        })

    return render_template(
        "film.html",
        film=film,
        regisseur=regisseur,
        rollen=rollen_met_acteurs
    )

# Movies
@app.route("/movies")
def movies():
    query = db.select(Film).order_by(Film.title.asc())
    filmslist = db.session.execute(query).scalars().all()
    return render_template("movies.html", filmslist=filmslist)


# Favorite toggle
@app.route("/favorite/<int:film_id>", methods=["POST"])
def favorite(film_id):
    user_id = session.get("user_id")
    if not user_id:
        flash("Je moet eerst inloggen om favorieten toe te voegen.", "warning")
        return redirect("/login")

    query = db.select(Favorite).filter_by(
        user_id=session["user_id"],
        film_id=film_id
    )

    #Omdat het een toggle is:
    favorite = db.session.execute(query).scalar_one_or_none()

    if favorite:
        db.session.delete(favorite)
        db.session.commit()
        flash("Film verwijderd uit favorieten.", "danger")
        return redirect("/myaccount")

    new_favorite = Favorite(
        user_id=session["user_id"],
        film_id=film_id 
    )
    db.session.add(new_favorite)
    db.session.commit()

    flash("Film toegevoegd aan favorieten!", "success")
    return redirect(url_for("film_pagina", film_id=film_id))
    #url_for genereert route functie op basis van film / film_id

@app.route("/search", methods=["GET"])
def search():
    # Haal zoekterm op uit de submit
    search = request.args.get("query")

    # Als er geen zoekterm is, geven we een lege lijst terug
    if not search:
        return render_template("search.html", results=[], query=search)

    # We zoeken naar films waarvan de titel ILIKE hoofdletterongevoelig dus!
    #f string zet de variabele om naar een string
    query = db.select(Film).where(Film.title.ilike(f"%{search}%"))
    results = db.session.execute(query).scalars().all()

    return render_template("search.html", results=results, query=search)

