from flask import Flask

# import the blueprints for the routes
from .views import views


def create_app():
    app = Flask("app")

    app.register_blueprint(views, url_prefix="/")
    return app