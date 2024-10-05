import uuid
from flask import Blueprint, render_template, redirect, url_for, request, flash
from .functions import db


edit_bp = Blueprint("edit", __name__)

@edit_bp.route("/edit/<id>", methods=["GET", "PUT", "POST"])
def edit(id):

    if request.method == "GET":
        return render_template("views/edit.html", contact=db.findContact(id))
        
    else:
        contact_name    = request.form.get("name")
        contact_surname = request.form.get("surname")
        contact_number  = request.form.get("number")

        if not (contact_name or contact_surname or contact_number ):
            flash("Nenhum campo foi preenchido.")
            return render_template("views/edit.html", contact=db.findContact(id))

        db.editContact(id, contact_name, contact_surname, contact_number)

        return redirect(url_for("home.home"))