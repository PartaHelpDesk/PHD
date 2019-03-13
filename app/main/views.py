from . import main_blueprint
from flask import render_template


@main_blueprint.route('/dashboard')
def dashboard():

    return render_template("dashboard.html")
