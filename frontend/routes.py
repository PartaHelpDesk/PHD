from frontend import frontend
from frontend.forms import EmailForm
from flask import render_template

@frontend.route('/')
@frontend.route('/index')
def index():
	return '''
<html>
  <style>
    .content {
      max-width:500px;
        margin: auto;
    }
  </style>
<head>
<title>PartaHelpDesk 1.0.0</title>
</head>
<body>
<div class="content">
<h1 >Welcome to the PHD Ticketing System</h1>
 <p>
  A ticketing system made for PARTA
  </p>
  <p>
    <a href="http://127.0.0.1:5000/login">Click Here to Login</a> 
    <a href="http://127.0.0.1:5000/email_test">Email Test</a>
  </p>
  </div>
</body>
</html>

'''

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

@frontend.route('/email_test')
def email_test():
	form = EmailForm()
	return '''
    <h1>Email Test</h1>
    <form action="" method="post" novalidate>
        {{ form.hidden_tag() }}
        <p>
            {{ form.rAddr.label }}
            {{ form.rAddr(size=32) }}
        </p>
        <p>
            {{ form.emailBody.label }}<br>
            {{ form.emailBody(size=32) }}
        </p>
        <p>{{ form.submit() }}</p>
    </form>
'''


