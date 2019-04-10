from frontend import frontend
from frontend.forms import EmailForm, TicketForm
from flask import render_template, flash, redirect
from backend import email_service, DatabaseMethods, Datatable, DataRow

@frontend.route('/')
@frontend.route('/index')
def index():
	user = {'username': 'PHD User'}
	return render_template('index.html', title='PartaHelpDesk 1.0.0', user=user)

@frontend.route('/login')
def login():
	return '''
<html>
<head>
<title>PHD Login</title>
</head>
<body>

<h1 >PHD Login Page</h1>
 <form>
  Email:<br>
  <input type="text" name="Email"><br>
  Password:<br>
  <input type="password" name="Password"> <br>
  <input type="submit" value="Submit">
</form> 
</body>
</html>
'''

@frontend.route('/ticket_submitted')
def ticket_submitted():
	return '''
<html>
<head>
<title>Submitted</title>
</head>
<body>

<h1 >Ticket Submitted!</h1>

</body>
</html>
'''

@frontend.route('/email_test', methods=['GET', 'POST'])
def email_test():
	form = EmailForm()
	user = {'username': 'PHD User'}
	if form.validate_on_submit():
		recipients = []
		recipients.append(form.rAddr.data)
		print(form.emailBody.data)
		email_service.send_email(None, "PartaHelpDesk@gmail.com", recipients, form.emailBody.data, None)
		return redirect('/index')
	return render_template('email.html', title='Email Testing', form=form, user=user)


@frontend.route('/create_ticket', methods=['GET', 'POST'])
def create_ticket():
	form =  TicketForm()
	user = {'username' : 'PHD User'}
	if form.validate_on_submit():
		# GET ALL IT LEVEL USERS AND APPEND THEM TO EMAIL RECIPIENT LIST
		recipients = []
		dbm = DatabaseMethods.DatabaseMethods()
		recipients = dbm.GetITEmails()
		print(form.ticketDescription.data)
		#tSubject = 'TicketTester'
		ticketTitle = form.ticketTitle.data
		tickDepartment = form.department.data
		ticketCategory = form.ticketCategory.data
		#ticketStatus = form.ticketStatus.data
		tickDescription = form.ticketDescription.data
		emailMessage = email_service.format_email(ticketTitle,tickDepartment,ticketCategory,'New',tickDescription)
		email_service.send_group_email("PartaHelpDesk@gmail.com", recipients, emailMessage, None)
		dbm.CreateTicket(ticketTitle,ticketCategory,133,'New',tickDepartment,tickDescription)
		return redirect('/ticket_submitted')
	return render_template('create_ticket.html', title='Create Ticket Test', form=form, user=user)