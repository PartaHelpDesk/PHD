from app import app

@app.route('/')
@app.route('/index')
def index():
	return '''
<html>
<head>
<title>PartaHelpDesk 1.0.0</title>
</head>
<body>

<h1 >PHD Login Page</h1>
 <form>
  Email:<br>
  <input type="text" name="Email"><br>
  Password:<br>
  <input type="text" name="Password"> <br>
  <input type="submit" value="Submit">
</form> 
</body>
</html>
'''

