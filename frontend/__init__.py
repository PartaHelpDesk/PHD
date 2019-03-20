from flask import Flask
from flask_mail import Mail
import os

frontend = Flask(__name__)
frontend.config['SECRET_KEY'] = 'you-will-never-guess'
frontend.config.update(dict(
	MAIL_SERVER='smtp.googlemail.com',
	MAIL_PORT=587,
	MAIL_USE_TLS=1,
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME'),
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	))

mail = Mail(frontend)

from frontend import routes