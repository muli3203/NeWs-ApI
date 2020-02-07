from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    app.config.from_pyfile('config.py')

    # Initializing flask extensions
    bootstrap.init_app(app)

    #registering blueplint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)

    return app