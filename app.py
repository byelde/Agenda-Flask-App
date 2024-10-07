from flask import Flask, redirect, render_template, url_for

def create_app():
    
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("views/home.html")


    @app.route("/add")
    def add():
        return render_template("views/add.html")


    @app.route("/edit/<id>") # Deve receber id
    def edit(id):
        return render_template("views/edit.html")
    

    @app.route("/delete/<id>") # Trocar por delete
    def remove(id):
        return redirect(url_for("home"))
    
    
    # @app.route("/exemplo/<args>")
    # def exemplo(args):
    #     return render_template("exemplo.html", dados=args)
    
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()