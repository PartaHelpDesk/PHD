from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/login')
def login():
    return "This will be the PHD login url"

@app.route('/dashboard')
def dashboard():
    return "This will be a customized dahboard"

