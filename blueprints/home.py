from flask import Blueprint, render_template
from .functions import db

home_bp = Blueprint("home", __name__)

@home_bp.route("/", methods=["GET"])
def home():
    return render_template("views/home.html", contacts=db.getContacts())