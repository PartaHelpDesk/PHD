from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name='default'):

    app = Flask(__name__)
    app.config.from_object(config.get(config_name))
    db.init_app(app)

    from app.user import user_blueprint
    app.register_blueprint(user_blueprint)

    from app.main import main_blueprint
    app.register_blueprint(main_blueprint)

    return app
