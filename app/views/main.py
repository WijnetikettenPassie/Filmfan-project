from flask import Blueprint, render_template, redirect, flash, request, session, url_for
from app import db
from app.models import Film

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

# Movies
@bp.route("/movies")
def movies():
    query = db.select(Film).order_by(Film.title.asc())
    filmslist = db.session.execute(query).scalars().all()
    return render_template("movies.html", filmslist=filmslist)

# Search
@bp.route("/search", methods=["GET"])
def search():
    search = request.args.get("query")

    if not search:
        return render_template("search.html", results=[], query=search)

    query = db.select(Film).where(Film.title.ilike(f"%{search}%"))
    results = db.session.execute(query).scalars().all()

    return render_template("search.html", results=results, query=search)