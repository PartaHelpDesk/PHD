from frontend import frontend
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from config import config

db = SQLAlchemy(frontend)
mail = Mail(frontend)
login_manager = LoginManager(frontend)
login_manager.login_message = 'Please log in before you do anything else.'
login_manager.session_protection = 'strong'
login_manager.login_view = 'login_2'

# load config
frontend.config.from_object(config.get('dev'))

from frontend import models
