from flask import Flask, render_template, redirect, url_for, request, flash
import db

app = Flask(__name__)
app.secret_key = "12345"


@app.route("/")
def home():
    return render_template("home.html", contacts=db.getContactList())


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        contact_name = request.form.get("name")
        contact_surname = request.form.get("surname")
        contact_number = request.form.get("number")

        if not (contact_name and contact_surname and contact_number):
            return render_template("add.html")

        if db.checkExists(contact_number):
            flash("numero ja registrado")
            return render_template("add.html")

        new_contact = {
            "name": contact_name,
            "surname": contact_surname,
            "number": contact_number,
        }

        db.saveNewContact(new_contact)

        return redirect(url_for("home"))


@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "GET":
        return render_template("edit.html")

    else:
        contact_name = request.form.get("name")
        contact_surname = request.form.get("surname")
        contact_number = request.form.get("number")

        if not (contact_name or contact_surname or contact_number):
            return render_template("edit.html")

        db.editContact(id, contact_name, contact_surname, contact_number)

        return redirect(url_for("home"))


@app.route("/remove/<id>", methods=["GET", "POST"])
def remove(id):
    if request.method != "GET":

        db.deleteContact(id)

    return redirect(url_for("home"))


app.run(debug=True)
