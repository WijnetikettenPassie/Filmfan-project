from flask import Blueprint, render_template, redirect, flash, request, session, url_for
from app import db
from app.models import Film, Rol, Acteur, Regisseur, Favorite, Rating

bp = Blueprint("films", __name__, url_prefix="/film")

# Film pagina
@bp.route("/<int:film_id>")
def film_pagina(film_id):
    film = Film.query.get_or_404(film_id)
    regisseur = Regisseur.query.get(film.regisseur_id)

    rollen = Rol.query.filter_by(film_id=film_id).all()

    rollen_met_acteurs = []
    for rol in rollen:
        acteur = Acteur.query.get(rol.acteur_id)
        rollen_met_acteurs.append({
            "personage": rol.personage,
            "acteur": acteur
        })

    query_avg = db.select(db.func.avg(Rating.value)).where(Rating.film_id == film_id)
    avg_result = db.session.execute(query_avg).scalar()

    average_rating = round(avg_result, 1) if avg_result else None

    user_id = session.get("user_id")

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

# Review
@bp.route("/review/<int:film_id>", methods=["POST"])
def review(film_id):

    user_id = session.get("user_id")

    if not user_id:
        flash("Je moet eerst inloggen om favorieten toe te voegen.", "warning")
        return redirect("/login")
    
    film = db.session.get(Film, film_id)
    rating_value = request.form.get("rating")

    if rating_value:
        query = (
            db.select(Rating)
            .where(Rating.film_id == film_id)
            .where(Rating.user_id == user_id)
        )

        result = db.session.execute(query)
        existing_rating = result.scalar_one_or_none()
        
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

    return redirect(url_for("films.film_pagina", film_id=film.id))

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
    return redirect(url_for("films.film_pagina", film_id=film_id))