from . import frontend
from flask import render_template, redirect, url_for, abort
from flask_login import login_required
from .utils import *
from frontend.models import Status, Category


@frontend.route('/dashboard')
@login_required
def dashboard_2():
    my_tickets = get_my_tickets()
    tickets_queue = get_tickets_queue()
    return render_template("ticket_queue.html", my_tickets=my_tickets, tickets_queue=tickets_queue)


@frontend.route('/')
@login_required
def index_2():
    return redirect(url_for('login_2'))


@frontend.route("/view_ticket/<int:ticket_id>")
@login_required
def view_ticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        abort(404)

    return render_template("view_ticket.html", t=ticket)


@frontend.route("/update_ticket/<int:ticket_id>", methods=["POST", "GET"])
@login_required
def update_ticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        abort(404)

    status = Status.query.all()

    return render_template("update_ticket.html", t=ticket, status=status)


@frontend.route("/edit_ticket/<int:ticket_id>", methods=["POST", "GET"])
@login_required
def edit_ticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        abort(404)
    status = Status.query.all()
    categories = Category.query.all()
    return render_template("edit_ticket.html", t=ticket, status=status, categories=categories)


@frontend.route("/view_all")
@login_required
def view_all():
    tickets = Ticket.query.all()
    return render_template("view_all.html", tickets=tickets)

@frontend.route("/create_ticket", methods=['GET', 'POST'])
@login_required
def create_ticket():
    return render_template("create_ticket.html")
