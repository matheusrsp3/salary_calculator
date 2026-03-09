from flask import Flask
from app.controllers.routes import register_routes

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    print(f"{app.root_path=}")
    register_routes(app)
    return app