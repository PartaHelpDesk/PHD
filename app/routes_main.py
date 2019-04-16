from . import app
from flask import render_template, redirect, url_for, abort
from flask_login import login_required
from .utils import *
from app.models import Status, Category
from app.forms import ReportForm
from app import report_service




@app.route('/dashboard')
@login_required
def dashboard():
    my_tickets = get_my_tickets()
    tickets_queue = get_tickets_queue()
    return render_template("ticket_queue.html", my_tickets=my_tickets, tickets_queue=tickets_queue)



@app.route("/view_ticket/<int:ticket_id>")
@login_required
def view_ticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        abort(404)

    return render_template("view_ticket.html", t=ticket)


@app.route("/update_ticket/<int:ticket_id>", methods=["POST", "GET"])
@login_required
def update_ticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        abort(404)

    status = Status.query.all()
    return render_template("update_ticket.html", t=ticket, status=status)


@app.route("/edit_ticket/<int:ticket_id>", methods=["POST", "GET"])
@login_required
def edit_ticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        abort(404)
    status = Status.query.all()
    categories = Category.query.all()
    return render_template("edit_ticket.html", t=ticket, status=status, categories=categories)


@app.route("/view_all")
@login_required
def view_all():
    tickets = Ticket.query.all()
    return render_template("view_all.html", tickets=tickets)


@app.route("/create_ticket", methods=['GET', 'POST'])
@login_required
def create_ticket():
    return render_template("create_ticket.html")

@app.route("/report_test", methods=['GET','POST'])
def report_test():
    form = ReportForm()
    if form.validate_on_submit():
        selection = { 'choice': form.reportChoice.data }
        if selection['choice'] == 'Category':
            report_service.report_by_category()
            return render_template("/view_report.html", selection=selection)
        if selection['choice'] == 'Department':
            report_service.report_by_department()
            return render_template("/view_report.html", selection=selection)
    return render_template("report_test.html", form=form)
