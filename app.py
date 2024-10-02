from flask import Flask
from .controllers import home_bp, add_bp, delete_bp, edit_bp

# create app
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "chave_super_secreta!@%^&"

    app.register_blueprint(home_bp)
    app.register_blueprint(add_bp)
    app.register_blueprint(delete_bp)
    app.register_blueprint(edit_bp)

    return app

if __name__ == "__main__":
    app = create_app()