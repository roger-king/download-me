"""
    Application
"""

from flask_api import FlaskAPI

from instance.config import APP_CONFIG

"""
    @docs
    @function create_app
    base function to create Flask application
"""


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(APP_CONFIG[config_name])
    app.config.from_pyfile('config.py')

    return app
