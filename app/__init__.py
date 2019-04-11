from flask import Flask
from flask_mail import Mail
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config.update(dict(
	MAIL_SERVER='smtp.googlemail.com',
	MAIL_PORT=587,
	MAIL_USE_TLS=1,
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME'),
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	))

mail = Mail(app)

from app import routes, routes_main, routes_user
from app import initialization
