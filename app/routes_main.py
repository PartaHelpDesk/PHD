from . import app
from flask import render_template, redirect, url_for, abort, request, flash
from flask_login import login_required, current_user
from app import DatabaseMethods as dm
from app.models import Tickets, User
from app.forms import ReportForm, TicketForm, EmailForm, PasswordResetForm, UpdateTicketForm, UpdatePasswordForm
from app import report_service, email_service
from random import randint


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
  ticket = Tickets.getTicketFromID(ticket_id)  
  return render_template("view_ticket.html", ticket=ticket)


@app.route("/update_ticket/<int:ticket_id>", methods=["POST", "GET"])
@login_required
def update_ticket(ticket_id):
    ticket = Tickets.getTicketFromID(ticket_id)
    form = UpdateTicketForm()
    #form.ticketComment = ticket.comment
    dbm = dm.DatabaseMethods()

    if request.method == 'POST':      
      selection = {
        'Department': form.ticketDepartment.data,
        'Title': form.ticketTitle.data,
        'Description': form.ticketDescription.data,
        'Category': form.ticketCategory.data,
        'Status': form.ticketStatus.data,
        'Comment': form.ticketComment.data
      }
      print(selection)
      dbm.UpdateTicket(current_user.user_id, ticket.ticket_id, selection['Title'], selection['Category'], selection['Status'], selection['Department'], selection['Description'], selection['Comment'])
      flash('Ticket has been updated!')
      return redirect(url_for('dashboard'))
  
    dt_c = dbm.GetCategories()
    dt_d = dbm.GetDepartments()

    form.ticketTitle.data = ticket.title
    form.ticketCategory.data = ticket.category
    form.ticketDepartment.data = ticket.department
    form.ticketDescription.data = ticket.description
    form.ticketStatus.data = ticket.status
    """
    Add junk entry this to deal with begining null entry
    we will have to handle this later in DB Methods because 
    it is not a valid category
    """
    categories = [('-','-')]
    for c in dt_c.data_rows:
        des = c.GetColumnValue('Description')
        categories.append((des, des))
    form.ticketCategory.choices = categories

    deparments = [('-','-')]
    for d in dt_d.data_rows:
      dep = d.GetColumnValue('Description')
      deparments.append((dep,dep))

    form.ticketDepartment.choices = deparments
    return render_template("update_ticket.html", form=form, ticket=ticket)


@app.route("/view_all/")
@login_required
def view_all():
  dbm = dm.DatabaseMethods()
  dt = dbm.GetTicketFiltered(None)
  t = Tickets()
  tickets = []
  for dr in dt.data_rows:
      tickets.append(t.createTicketObject(dr))
  return render_template("view_queue.html", tickets=tickets)


@app.route("/view_all_filter", methods=["POST"])
@login_required
def view_all_filter():
  dbm = dm.DatabaseMethods()
  filter_text = request.form.get("filter_text")
  dt = dbm.GetTicketFiltered(filter_text)
  print ('here')
  t = Tickets()
  tickets = []
  for dr in dt.data_rows:
      tickets.append(t.createTicketObject(dr))
  return render_template("view_queue.html", tickets=tickets)



@app.route("/create_ticket", methods=['GET', 'POST'])
@login_required
def create_ticket():
  
  form = TicketForm()
  dbm = dm.DatabaseMethods()

  if request.method == 'POST':      
    selection = {
      'Department': form.ticketDepartment.data,
      'Title': form.ticketTitle.data,
      'Description': form.ticketDescription.data,
      'Category': form.ticketCategory.data
    }
    recipients = dbm.GetITEmails()
    dbm.CreateTicket(selection['Title'],selection['Category'], current_user.user_id,'New',selection['Department'],selection['Description'])
    emailMessage = email_service.format_email(selection['Title'],selection['Department'],selection['Category'],'New',selection['Description'])
    email_service.send_group_email("PartaHelpDesk@gmail.com", recipients, emailMessage, None, selection['Title'])
    return redirect(url_for('dashboard'))
 
  dbm = dm.DatabaseMethods()
  dt_c = dbm.GetCategories()
  dt_d = dbm.GetDepartments()
  
  """
  Add junk entry this to deal with begining null entry
  we will have to handle this later in DB Methods because 
  it is not a valid category
  """
  categories = [('-','-')]
  for c in dt_c.data_rows:
      des = c.GetColumnValue('Description')
      categories.append((des, des))
  form.ticketCategory.choices = categories

  deparments = [('-','-')]
  for d in dt_d.data_rows:
    dep = d.GetColumnValue('Description')
    deparments.append((dep,dep))

  form.ticketDepartment.choices = deparments
  return render_template("create_ticket.html", form=form)

@app.route("/reporting", methods=['GET','POST'])
@login_required
def reporting():
    form = ReportForm()
    if form.validate_on_submit():
        selection = { 'choice': form.reportChoice.data }
        if selection['choice'] == 'Category':
            fileSavePath = report_service.report_by_category()
            return render_template("/view_report.html", selection=selection, fileSavePath=fileSavePath)
        if selection['choice'] == 'Department':
            fileSavePath = report_service.report_by_department()
            return render_template("/view_report.html", selection=selection, fileSavePath=fileSavePath)
        if selection['choice'] == 'Status':
            fileSavePath = report_service.report_by_status()
            return render_template("/view_report.html", selection=selection, fileSavePath=fileSavePath)
    return render_template("reporting.html", form=form)

@app.route("/password_reset", methods=['GET','POST'])
def password_reset():
  form = PasswordResetForm()
  if form.validate_on_submit():
    dbm = dm.DatabaseMethods()  
    accountName = form.accUsername.data
    user = User(accountName)
    newpass = dbm.GenerateRandomPassword()
    passMessage = "Your New Password is: " + newpass
    recip = []
    recip.append(user.email)
    email_service.send_email("Password Reset","partahelpdesk@gmail.com",recip,passMessage, None)
    dbm.UpdateUserPassword(accountName, newpass)
    flash('Email With New Password Sent')
    return redirect(url_for('login'))
  return render_template("password_reset.html", form=form)

@app.route("/update_password", methods=['GET','POST'])
def update_password():
  form = UpdatePasswordForm()
  dbm = dm.DatabaseMethods()  

  if form.validate_on_submit():
    old_password = form.oldpassword.data
    new_password = form.newpassword.data
    verify_password = form.verifypassword.data

    if verify_password != new_password or not dbm.CheckUserPassword(current_user.username, old_password):
      return redirect(url_for("update_password"))

    else:  
      dbm.UpdateUserPassword(current_user.username, new_password)
      passMessage = "The password for this account has been updated"
      recip = []
      recip.append(current_user.email)
      email_service.send_email("Password Reset","partahelpdesk@gmail.com",recip,passMessage, None)
      flash('Password succesfully changed!')
      return render_template("account.html")


  return render_template("update_password.html", form=form)
