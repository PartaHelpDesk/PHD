from frontend import frontend
from flask import render_template, request

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

@frontend.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template('login.html')
  else:
    return request.form


