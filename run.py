from flask import Flask
from .controllers import get_controller
from .controllers import post_controller
from .controllers import delete_controller
from .controllers import put_controller


def register_controllers_routes(app):
    app.register_blueprint(get_controller.routes)
    app.register_blueprint(post_controller.routes)
    app.register_blueprint(delete_controller.routes)
    app.register_blueprint(put_controller.routes)

app = Flask( __name__ )
register_controllers_routes(app)

if __name__ == '__run__':

    app.run(debug=True, host='0.0.0.0', port=5000)