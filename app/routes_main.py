from . import app
from flask import render_template, redirect, url_for, abort
from flask_login import login_required
from .utils import *
from app.models import Status, Category


@app.route('/hliu32/dashboard')
@login_required
def dashboard_2():
    my_tickets = get_my_tickets()
    tickets_queue = get_tickets_queue()
    return render_template("ticket_queue.html", my_tickets=my_tickets, tickets_queue=tickets_queue)


@app.route('/hliu32')
@login_required
def index_2():
    return redirect(url_for('login_2'))


@app.route("/hliu32/view_ticket/<int:ticket_id>")
@login_required
def view_ticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        abort(404)

    return render_template("view_ticket.html", t=ticket)


@app.route("/hliu32/update_ticket/<int:ticket_id>", methods=["POST", "GET"])
@login_required
def update_ticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        abort(404)

    status = Status.query.all()

    return render_template("update_ticket.html", t=ticket, status=status)


@app.route("/hliu32/edit_ticket/<int:ticket_id>", methods=["POST", "GET"])
@login_required
def edit_ticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        abort(404)
    status = Status.query.all()
    categories = Category.query.all()
    return render_template("edit_ticket.html", t=ticket, status=status, categories=categories)


@app.route("/hliu32/view_all")
@login_required
def view_all():
    tickets = Ticket.query.all()
    return render_template("view_all.html", tickets=tickets)
