from flask import Flask
from . import auth

def init_app(app: Flask) -> None:
    app.register_blueprint(auth.bp)