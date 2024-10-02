from flask import Blueprint, redirect, url_for
from .functions import db

delete_bp = Blueprint("delete", __name__)

@delete_bp.route("/delete/<id>", methods=["GET","DELETE"])
def delete(id):
    db.deleteContact(id)
    return redirect(url_for("home.home"))