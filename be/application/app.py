from flask import Flask
from flask_restful import Api

from .resources import MainPageResource


def register_routes(api):
    api.add_resource(MainPageResource, '/')


def create_app():
    app = Flask(__name__)
    api = Api(app)
    register_routes(api)
    return app

