from . import frontend
from flask import render_template, redirect, url_for, abort
from flask_login import login_required
from .utils import *


@frontend.route('/hliu32/dashboard')
@login_required
def dashboard_2():
    my_tickets = get_my_tickets()
    tickets_queue = get_tickets_queue()
    return render_template("ticket_queue.html", my_tickets=my_tickets, tickets_queue=tickets_queue)


@frontend.route('/hliu32')
@login_required
def index_2():
    return redirect(url_for('login_2'))


@frontend.route("/hliu32/view_ticket/<int:ticket_id>")
@login_required
def view_ticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        abort(404)

    return render_template("view_ticket.html", t=ticket)
