from . import app
from flask import render_template, redirect, url_for, abort, request
from flask_login import login_required, current_user
from app import DatabaseMethods as dm
from app.models import Tickets, User
from app.forms import ReportForm
from app import report_service


@app.route('/dashboard')
@login_required
def dashboard():
    show_ticket_queue = False
    t = Tickets()
    tickets_queue = None
    if current_user.level != '1':
        tickets_queue = t.getTicketQueue()
        show_ticket_queue = True
    user_tickets_queue = t.getAllUserTicket(current_user.user_id)
    return render_template("dashboard.html", tickets_queue=tickets_queue, my_tickets=user_tickets_queue, show_ticket_queue=show_ticket_queue)


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
    return render_template("view_all.html")


@app.route("/create_ticket", methods=['GET', 'POST'])
@login_required
def create_ticket():
  form = forms.TicketForm()
  if request.method == 'POST' and form.validate():
    params = (form.ticketTitle, form.department, form.ticketCategory, form.ticketDescription)
    
  return render_template("create_ticket.html", form=form)

@app.route("/report_test", methods=['GET','POST'])
def report_test():
    form = ReportForm()
    if form.validate_on_submit():
        selection = { 'choice': form.reportChoice.data }
        if selection['choice'] == 'Category':
            fileSavePath = report_service.report_by_category()
            return render_template("/view_report.html", selection=selection, fileSavePath=fileSavePath)
        if selection['choice'] == 'Department':
            fileSavePath = report_service.report_by_department()
            return render_template("/view_report.html", selection=selection, fileSavePath=fileSavePath)
    return render_template("report_test.html", form=form)

