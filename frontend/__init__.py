from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from config import config


frontend = Flask(__name__)
db = SQLAlchemy(frontend)
mail = Mail(frontend)
login_manager = LoginManager(frontend)
login_manager.login_message = 'Please log in before you do anything else.'
login_manager.session_protection = 'strong'
login_manager.login_view = 'user.login'

from frontend import routes, main_routes, user_routes
