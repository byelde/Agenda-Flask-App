from flask import Flask, redirect, render_template, request, url_for

def create_app():
    
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def home():
        return render_template("views/home.html")


    @app.route("/add", methods=["GET", "POST"])
    def add():

        if request.method == "GET":
            return render_template("views/add.html")
    
        else:
            contact_name    = request.form.get("name")
            contact_surname = request.form.get("surname")
            contact_number  = request.form.get("number")

            if not (contact_name and contact_surname and contact_number):
                # Flash/Pop-Up
                return render_template("views/add.html")
            
            new_contact = {
                "name": contact_name,
                "surname": contact_surname,
                "number": contact_number
            }

            print(new_contact)

            # Checar no bd se o numero já está registrado

            # Salvar numero no bd

            return redirect(url_for("home"))


    @app.route("/edit/<id>", methods=["GET", "POST"]) # Deve receber id
    def edit(id):
        if request.method == "GET":
            return render_template("views/edit.html") # Adicionar contact (como esta no html)
            
        else:
            contact_name    = request.form.get("name")
            contact_surname = request.form.get("surname")
            contact_number  = request.form.get("number")

            if not (contact_name or contact_surname or contact_number ):
                # Flash/Pop-Up
                return render_template("views/edit.html") # Adicionar contact (como esta no html)

            print(contact_name, contact_surname, contact_number)

            # Editar contato no banco de dados

            return redirect(url_for("home"))
    

    @app.route("/delete/<id>", methods=["GET", "DELETE"]) # Trocar por delete
    def remove(id):
        if request.method == "DELETE":
            print("removeu!!")
            pass
            # remover contato do banco de dados
        
        return redirect(url_for("home"))

    
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()