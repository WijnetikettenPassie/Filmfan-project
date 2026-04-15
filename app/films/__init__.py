from flask import Blueprint

bp = Blueprint("films", __name__, url_prefix="/film", template_folder="templates")

from app.films import routes