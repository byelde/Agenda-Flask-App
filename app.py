from flask import Flask, redirect, render_template, request, url_for

def create_app():
    
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def home():
        # carregar a pagina
        return render_template("home.html")


    @app.route("/add", methods=["GET", "POST"])
    def add():

        if request.method == "GET":
            # carregar a pagina
            return render_template("add.html")
    
        else:
            # recolher o conteudo dos campos
            contact_name    = request.form.get("name")
            contact_surname = request.form.get("surname")
            contact_number  = request.form.get("number")

            # caso algum campo esteja vazio
            if not (contact_name and contact_surname and contact_number):
                # Flash/Pop-Up
                # carregar a pagina novamente para ser preenchida
                return render_template("add.html")
            
            # estruturar um novo contato
            new_contact = {
                "name": contact_name,
                "surname": contact_surname,
                "number": contact_number
            }
            # Checar no bd se o numero já está registrado
            # ...

            # Salvar numero no bd
            #...

            # retornar para a home page
            return redirect(url_for("home"))


    @app.route("/edit/<id>", methods=["GET", "POST"]) # ----> Trocar por delete, que, por algum motivo, nao esta funcionando
    def edit(id):
        if request.method == "GET":
            # carregar a pagina
            return render_template("edit.html") # Adicionar contact (como esta no html)
            
        else:
            # recolher o conteudo dos campos
            contact_name    = request.form.get("name")
            contact_surname = request.form.get("surname")
            contact_number  = request.form.get("number")

            # Caso nenhum campo esteja preenchido
            if not (contact_name or contact_surname or contact_number ):
                # Flash/Pop-Up
                # carregar pagina para ser preenchida novamente
                return render_template("edit.html") # Adicionar contact (como esta no html)

            # Editar contato no banco de dados
            # ...

            # Direcionar para home page
            return redirect(url_for("home"))
    

    @app.route("/delete/<id>", methods=["GET", "POST"]) # ----> Trocar por delete, que, por algum motivo, nao esta funcionando
    def remove(id):
        if request.method == "DELETE":
            # remover contato do banco de dados
            # ...
            print("removeu")
            pass
        
        return redirect(url_for("home"))

    
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()