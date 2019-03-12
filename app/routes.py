from app import app

@app.route('/')
@app.route('/index')
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
  </p>
  </div>
</body>
</html>

'''

@app.route('/login')
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