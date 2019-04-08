from flask import Flask
from flask_mail import Mail

frontend = Flask(__name__)
mail = Mail(frontend)

from frontend import user_routes, main_routes
from frontend import initialization
