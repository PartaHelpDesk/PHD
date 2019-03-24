from . import main_blueprint
from flask import render_template, redirect, url_for
from flask_login import login_required
from .service import *


@main_blueprint.route('/dashboard')
@login_required
def dashboard():
    my_tickets = get_my_tickets()
    tickets_queue = get_tickets_queue()
    return render_template("dashboard.html", my_tickets=my_tickets, tickets_queue=tickets_queue)


@main_blueprint.route('/')
@login_required
def index():
    return redirect(url_for('user.login'))
