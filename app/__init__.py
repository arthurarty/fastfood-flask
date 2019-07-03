from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from instance.config import app_config
from flask_jwt_extended import JWTManager

db = SQLAlchemy()


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    JWTManager(app)

    from . import auth, menu, order
    app.register_blueprint(auth.bp)
    app.register_blueprint(menu.bp)
    app.register_blueprint(order.bp)

    return app
