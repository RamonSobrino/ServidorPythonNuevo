from flask import Flask
from flask_cors import CORS
from .controllers import get_controller
from .controllers import post_controller
from .controllers import delete_controller
from .controllers import put_controller

__author__ = 'Ramon Sobrino'


def register_controllers_routes(app):
    app.register_blueprint(get_controller.routes)
    app.register_blueprint(post_controller.routes)
    app.register_blueprint(delete_controller.routes)
    app.register_blueprint(put_controller.routes)


def create_app():
    app = Flask(__name__)
    cors = CORS(app)
    register_controllers_routes(app)
    return app
