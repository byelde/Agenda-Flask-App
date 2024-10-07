from flask import Flask

def create_app():
    
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "<h1>home page</h1>"


    @app.route("/add")
    def add():
        return "<h1>adicionar contato</h1>"


    @app.route("/edit")
    def edit():
        return "<h1>editar contato</h1>"
    
    @app.route("/remove")
    def remove():
        return "<h1>remover contato</h1>"
    
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()