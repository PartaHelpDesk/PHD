from flask import Flask
from flask_mail import Mail

frontend = Flask(__name__)
mail = Mail(frontend)

from frontend import routes