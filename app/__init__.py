from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_message = 'Please log in before you do anything else.'
login_manager.session_protection = 'strong'
login_manager.login_view = 'user.login'


def create_app(config_name='default'):

    # Initialize application
    app = Flask(__name__)
    app.config.from_object(config.get(config_name))
    db.init_app(app)
    login_manager.init_app(app)

    from app.main import main_blueprint
    app.register_blueprint(main_blueprint)

    from app.user import user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/user')
    return app
