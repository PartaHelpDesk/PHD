from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

mail = Mail(app)
login_manager = LoginManager(app)
login_manager.login_message = 'Please log in.'
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'

# load config
import models

#frontend.config.from_object(config.get('dev'))

