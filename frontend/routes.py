from frontend import frontend
from frontend.forms import EmailForm
from flask import render_template, flash, redirect
from backend import email_service

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

@frontend.route('/email_test', methods=['GET', 'POST'])
def email_test():
	form = EmailForm()
	user = {'username': 'PHD User'}
	if form.validate_on_submit():
		#flash('Email sent to {}'.format(form.rAddr.data))
		recipients = []
		recipients.append(form.rAddr.data)
		print(form.emailBody.data)
		email_service.send_email(None, "PartaHelpDesk@gmail.com", recipients, form.emailBody.data, None)
		return redirect('/index')
	return render_template('email.html', title='Email Testing', form=form, user=user)


@frontend.route('/create_ticket', methods=['GET', 'POST'])
def create_ticket():
	return '''
	<html>
<style>
.content {
  max-width: 500px;
  margin: auto;
}
  
#tickForm {
  display: none;
  align: center;
}
  
 #f1 {
   width: 100%;
   align: center;
}
  
</style>
<body class="content">
<h1>Create a Ticket Test:</h1>
<button onclick="startTicket()">Start a Ticket</button><br><br>
<div id="tickForm">
<form>
  <fieldset id="f1">
    <legend>Ticket Information</legend>
  </fieldset>
  </form>
</div>
</body>
<script>
function startTicket() {
  var x = document.getElementById("tickForm");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}
</script>
</html>
 '''

