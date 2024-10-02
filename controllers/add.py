import uuid
from flask import Blueprint, render_template, redirect, url_for, request, flash
from .functions import db


add_bp = Blueprint("add", __name__)

@add_bp.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "GET":
        flash("")
        return render_template("views/add.html")
    
    else:
        contact_name    = request.form.get("name")
        contact_surname = request.form.get("surname")
        contact_number  = request.form.get("number")

        if not (contact_name and contact_surname and contact_number ):
            flash("Preencha todos os campos.")
            return render_template("views/add.html")
        
        new_contact = {
            "id": 0,
            "name": contact_name,
            "surname": contact_surname,
            "number": contact_number
        }

        if db.checkExists(new_contact):
            flash("Number already registered.")
            return render_template("views/add.html")

        new_contact["id"] = str(uuid.uuid4())

        db.saveNewContact(new_contact)

        return redirect(url_for("home.home"))