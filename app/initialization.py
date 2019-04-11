from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from config import config
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base



frontend.config.from_object(config.get('dev'))

db = SQLAlchemy(frontend)
mail = Mail(frontend)
login_manager = LoginManager(frontend)
login_manager.login_message = 'Please log in.'
login_manager.session_protection = 'strong'
login_manager.login_view = 'login_2'

# load config
#frontend.config.from_object(config.get('dev'))

def init_db():
    import models
    Base.create_all(bind=engine)
