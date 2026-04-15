from flask import render_template, redirect,request, flash, session, current_app
from app import db
from app.users.forms import LoginForm, RegistrationForm, PasswordChangeForm
from app.models import User, Film, UserFavoriteRating
from app.users import bp
from werkzeug.security import generate_password_hash

# Login
@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        try:
            query = db.select(User).filter_by(email=form.email.data)
            user = db.session.execute(query).scalar_one_or_none()

            if user is None or not user.check_wachtwoord(form.wachtwoord.data):
                flash("Email of wachtwoord klopt niet", "danger")
                current_app.logger.info(f"Login poging mislukte voor email: {form.email.data}")
                return render_template("login.html", form=form)

            session["user_id"] = user.id
            session["username"] = user.username
            flash("Login succesvol!", "success")
            current_app.logger.info(f"Login succesvol voor gebruiker: {user.username} (ID: {user.id})")
            return redirect("/")
        except Exception as e:
            current_app.logger.error(f"Fout bij inloggen: {e}")
            flash("Er ging iets mis tijdens het inloggen. Probeer het later opnieuw.", "danger")
            return render_template("login.html", form=form)

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
            current_app.logger.info(f"Nieuwe gebruiker geregistreerd: {user.username} (ID: {user.id})")

        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f"Fout bij registreren: {e}")
            flash("Er ging iets mis tijdens het registreren. Probeer het later opnieuw.", "danger")
            return render_template("registreren.html", form=form)

        # Sla de gegevens op in de sessie
        session["user_id"] = user.id
        session["username"] = user.username

        # Succesbericht naar de gebruiker
        flash("Registratie succesvol!", "success")

        # Log de succesvolle registratie 
        current_app.logger.info(f"Gebruiker {user.username} (ID: {user.id}) is succesvol ingelogd na registratie.")

        return redirect("/myaccount")

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

    #Haalt usergegevens op om weer te geven
    query_udata = (db.select(User.email, User.geboortedatum,).where(User.id == user_id))
    user_data = db.session.execute(query_udata).one_or_none()


    return render_template("myaccount.html", favorites=favorites,user_data=user_data)

#Deze functie maakt account deletion mogelijk
@bp.route("/accountdel")
def delaccount():
    user_id = session.get("user_id")

    #Lijkt onnodig maar wat als gebruiker /accountdel in de url stopt
    #Beetje vreemd gedrag dus daarom hierbij ook een log
    if user_id == None:
        return redirect("/login")

    #Check of user wel bestaat in de database (good practice)
    query = db.select(User).where(User.id == user_id)
    user = db.session.execute(query).scalar_one_or_none()
    if not user:
        return redirect("/")

    #Zo ja ....
    db.session.delete(user)
    db.session.commit()
    session.clear()

    return redirect("/")

#Deze functie maakt het mogelijk je wachtwoord aan te passen
#Deze functie is gemixt geschreven door mij en AI, ik kwam er niet helemaal uit
@bp.route("/wwveranderen", methods=["GET", "POST"])
def wwveranderen():
    user_id = session.get("user_id")
    if not user_id:
        return redirect("/login")

    form = PasswordChangeForm()

    query = db.select(User).where(User.id == user_id)
    user = db.session.execute(query).scalar_one_or_none()

    if request.method == "GET":
        return render_template("wwveranderen.html", form=form)

    # Form validatie
    if not form.validate_on_submit():
        # voorkom dubbele foutmeldingen
        form.old_password.errors.clear()
        return render_template("wwveranderen.html", form=form)

    # Check oud wachtwoord
    if not user.check_wachtwoord(form.old_password.data):
        flash("Huidig wachtwoord is onjuist", "danger")
        return render_template("wwveranderen.html", form=form)

    # Nieuw wachtwoord opslaan
    user.wachtwoord = generate_password_hash(form.new_password.data)
    db.session.commit()

    flash("Wachtwoord succesvol gewijzigd", "success")
    return redirect("/myaccount")



        