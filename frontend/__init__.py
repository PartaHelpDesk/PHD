from flask import Flask
from flask_mail import Mail

frontend = Flask(__name__)
frontend.config['SECRET_KEY'] = 'you-will-never-guess'
mail = Mail(frontend)

from frontend import routes