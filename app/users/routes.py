from flask import render_template, redirect, flash,session
from app.users.forms import LoginForm, RegistrationForm
from app.models import User, Film, UserFavoriteRating
from app import db
from app.users import bp

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

# Logout
@bp.route("/logout", methods=["GET", "POST"])
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

    query = (
        db.select(UserFavoriteRating, Film)
        .join(Film, Film.id == UserFavoriteRating.film_id)
        .where(UserFavoriteRating.user_id == user_id)
    )
    favorites = db.session.execute(query).all()

    return render_template("myaccount.html", favorites=favorites)