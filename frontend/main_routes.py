from . import frontend
from flask import render_template, redirect, url_for
from flask_login import login_required
from .utils import *


@frontend.route('/hliu32/dashboard')
@login_required
def dashboard():
    my_tickets = get_my_tickets()
    tickets_queue = get_tickets_queue()
    return render_template("dashboard.html", my_tickets=my_tickets, tickets_queue=tickets_queue)


@frontend.route('/hliu32')
@login_required
def index_2():
    return redirect(url_for('login'))
