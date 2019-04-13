from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from config import config

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app.config.from_object(config.get('dev'))

db = SQLAlchemy(app)
mail = Mail(app)
login_manager = LoginManager(app)
login_manager.login_message = 'Please log in.'
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'

# load config
from app import models

#frontend.config.from_object(config.get('dev'))
