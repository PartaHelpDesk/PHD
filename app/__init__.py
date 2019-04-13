from flask import Flask
from flask_mail import Mail


app = Flask(__name__)
mail = Mail(app)

from app import routes_main, routes_user
from app import initialization

