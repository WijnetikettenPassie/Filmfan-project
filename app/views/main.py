from flask import Blueprint, render_template, redirect, flash, request, session, url_for
from app import db
from app.forms import LoginForm, RegistrationForm
from app.models import User, Film, Rol, Acteur, Regisseur, Favorite, Rating, UserFavoriteRating

bp = Blueprint("main", __name__)

#TO DO:
#Database revisen
#Hash de rest van de gegevens
#Maak de opdracht filmfan af MEGAIMPORTANT
    #Subissue maak een comment section
#fix de reigssuer + releasedate tekst

# Homepage
@bp.route("/")
def home():
    return render_template("home.html")

# Login
@bp.route("/login", methods=["GET", "POST"])
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
@bp.route("/logout", methods = ["GET","POST"])
def logout():
    session.clear()
    return redirect("/")

# Registreren
@bp.route("/register", methods=["GET", "POST"])
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
@bp.route("/myaccount")
def myaccount():
    user_id = session.get("user_id")

    if not user_id:
        flash("Je moet eerst inloggen om je account te zien.", "warning")
        return redirect("/login")

    #Haal de favorieten en ratings uit een view
    query = (
        db.select(UserFavoriteRating, Film).join(Film, Film.id == UserFavoriteRating.film_id).where(UserFavoriteRating.user_id == user_id)
    )
    favorites = db.session.execute(query).all()

    return render_template("myaccount.html", favorites=favorites)

# Film pagina
@bp.route("/film/<int:film_id>")
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

    #Query de database voor alle user ratings bij deze film en bereken een average
    query_avg = db.select(db.func.avg(Rating.value)).where(Rating.film_id == film_id)
    
    avg_result = db.session.execute(query_avg).scalar()

    #Zet het resultaat van de vorige query om in een afgerond cijfer ALS er een rating bestaat
    average_rating = round(avg_result, 1) if avg_result else None

    #Haal user_id op uit de session
    user_id = session.get("user_id")

    #Query de rating van de user
    query_user = db.select(Rating.value).where(Rating.film_id == film_id).where(Rating.user_id == user_id)
    
    user_rating = db.session.execute(query_user).scalar_one_or_none()

    return render_template(
        "film.html",
        film=film,
        regisseur=regisseur,
        rollen=rollen_met_acteurs,
        average_rating=average_rating,
        user_rating=user_rating
    )

@bp.route("/review/<int:film_id>", methods=["POST"])
def review(film_id):

    #Haal gegevens op uit de database
    user_id = session.get("user_id")

    #Check of deze persoon is ingelogd
    if not user_id:
        flash("Je moet eerst inloggen om favorieten toe te voegen.", "warning")
        return redirect("/login")
    
    film = db.session.get(Film, film_id)
    rating_value = request.form.get("rating")

    #Als er een rating verstuurd is (zou zo moeten zijn natuurlijk)
    if rating_value:
        query = (
            db.select(Rating)
            .where(Rating.film_id == film_id)
            .where(Rating.user_id == user_id)
        )

        result = db.session.execute(query)
        existing_rating = result.scalar_one_or_none()
        
        #Check of de gebruiker al een rating heeft
        #Optie 1 --> gebruiker heeft het al dan overwrite die rating en flash een message
        #Optie 2 --> Voeg een nieuwe rating toe aan de database en flash een message
        if existing_rating:
            existing_rating.value = int(rating_value)
            flash("Je beoordeling is gewijzigd!", "success")
        else:
            new_rating = Rating(
                value=int(rating_value),
                film_id=film.id,
                user_id=user_id
            )
            db.session.add(new_rating)
            flash("Beoordeling toegevoegd!", "success")

        db.session.commit()

    return redirect(url_for("main.film_pagina", film_id=film.id))

# Movies
@bp.route("/movies")
def movies():
    query = db.select(Film).order_by(Film.title.asc())
    filmslist = db.session.execute(query).scalars().all()
    return render_template("movies.html", filmslist=filmslist)

# Favorite toggle
@bp.route("/favorite/<int:film_id>", methods=["POST"])
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
    return redirect(url_for("main.film_pagina", film_id=film_id))

@bp.route("/search", methods=["GET"])
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