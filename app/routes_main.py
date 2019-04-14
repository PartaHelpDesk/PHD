from . import app
from flask import render_template, redirect, url_for, abort
from flask_login import login_required, current_user
from app import DatabaseMethods as dm
from app.models import Tickets, User


@app.route('/dashboard')
@login_required
def dashboard():
    #my_tickets = Tickets.getAllUserTicket(current_user.username)
    t = Tickets()
    tickets_queue = t.getTicketQueue()
    dbm = dm.DatabaseMethods()
    dt = dbm.GetAllUserTickets(current_user.user_id)
    dt.PrintValues()
    user_tickets_queue = t.getAllUserTicket(current_user.user_id)
    return render_template("dashboard.html", tickets_queue=tickets_queue, my_tickets=user_tickets_queue)


@app.route("/view_ticket/<int:ticket_id>")
@login_required
def view_ticket(ticket_id):
    # ticket = Ticket.query.get(ticket_id)
    # if not ticket:
    #     abort(404)

    return render_template("view_ticket.html", t=ticket)


@app.route("/update_ticket/<int:ticket_id>", methods=["POST", "GET"])
@login_required
def update_ticket(ticket_id):
    # ticket = Ticket.query.get(ticket_id)
    # if not ticket:
    #     abort(404)

    # status = Status.query.all()
    return render_template("update_ticket.html", t=ticket, status=status)


@app.route("/edit_ticket/<int:ticket_id>", methods=["POST", "GET"])
@login_required
def edit_ticket(ticket_id):
    # ticket = Ticket.query.get(ticket_id)
    # if not ticket:
    #     abort(404)
    # status = Status.query.all()
    # categories = Category.query.all()
    return render_template("edit_ticket.html", t=ticket, status=status, categories=categories)


@app.route("/view_all")
@login_required
def view_all():
    # tickets = Ticket.query.all()
    return render_template("view_all.html", tickets=tickets)


@app.route("/create_ticket", methods=['GET', 'POST'])
@login_required
def create_ticket():
    return render_template("create_ticket.html")