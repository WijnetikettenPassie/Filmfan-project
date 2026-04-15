from flask import render_template,request
from app import db
from app.models import Film,Rating

from app.main import bp   

# Homepage
@bp.route("/")
def home():
    # Genereerd dynamisch de average rating voor soldaat van Oranje
    query = db.select(Rating.value).where(Rating.film_id == 1)
    rating = db.session.execute(query).scalar()
    if rating is not None:
        return render_template("home.html", rating=rating)
    else:
        return render_template("home.html", rating=5)

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