from frontend import frontend
from flask import render_template, request, redirect, url_for

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
  if request.method == 'POST':
    
    username = request.form['username']
    password = request.form['password']
    error = None

    if not username:
      error = 'Must enter username'
    elif not password:
      error = 'Must enter password'
    if error is None:
      return redirect(url_for('dashboard'))   
  return render_template('login.html')


@frontend.route('/dashboard', methods=['GET','POST'])
def dashboard():
  return render_template('dashboard.html')