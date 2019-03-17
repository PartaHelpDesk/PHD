from . import main_blueprint
from flask import render_template
from flask_login import login_required
from .service import *


@main_blueprint.route('/dashboard')
@login_required
def dashboard():
    my_tickets = get_my_tickets()
    tickets_queue = get_tickets_queue()
    return render_template("dashboard.html", my_tickets=my_tickets, tickets_queue=tickets_queue)
