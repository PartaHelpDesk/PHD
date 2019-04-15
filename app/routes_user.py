from app.models import User
from flask import render_template, redirect, url_for, request, flash, abort
from flask_login import login_user, logout_user, current_user, login_required
from . import app
from app import DatabaseMethods as DM
from werkzeug.security import generate_password_hash


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        dbm = DM.DatabaseMethods()

        if dbm.CheckUserPassword(username, password):
            user = User(username)
            user.authenticated =True 
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed, user not found.')
            return redirect(url_for('login'))
         
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    current_user.authenticated = False
    logout_user(current_user)
    return redirect(url_for('login'))


@app.route('/users')
@login_required
def users():
    dbm = DM.DatabaseMethods()
    active_users = dbm.GetAllUsers(1) 
    print(active_users)
    inactives_users = dbm.GetAllUsers(0) 
    return render_template('users.html', active_users=active_users, inactive_users=inactives_users)


@app.route('/add_user', methods=["POST", "GET"])
@login_required
def add_user():
    if request.method == 'POST':
        
        dbm = DM.DatabaseMethods()
        username = request.form.get('username')
        first_name = request.form.get('first_name')
        last_name= request.form.get('last_name')
        email = request.form.get('email_address')
        level = request.form.get('user_level')

        if username == '' or first_name == '' or last_name == '' or email == '':
            flash('Please enter in all fields')
            return render_template('add_user.html')
        
        result = dbm.CreateUserAccount(username, level, first_name, last_name, email)

        flash(result)
        if result != 'Success':
            return render_template('add_user.html')

        return redirect(url_for("users"))

    return render_template('add_user.html')
        
      
    

@app.route("/edit_user/<int:id>", methods=["POST", "GET"])
@login_required
def edit_user(id):
    dbm = DM.DatabaseMethods()
    username = dbm.GetUsername(id)
    user = User(username)
    if not user:
        abort(404)
    if request.method == "POST":
        new_username = request.form.get("username")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get('email_address')
        level = request.form.get('level')

        print(first_name, last_name, email, level)
        if new_username == '' or first_name == '' or last_name == '' or email == '':
            flash('Incomplete user information. Please check!')
            return render_template("edit_user.html", u=user)

        result = dbm.UpdateUserAccount(id, new_username, level, first_name, last_name, email)

        flash(result)
        if result != 'Success':
            return render_template("edit_user.html", u=user)

        return redirect(url_for("users"))

    return render_template("edit_user.html", u=user)


@app.route("/deactive/<int:id>", methods=["POST"])
@login_required
def deactive(id):

    user = User.query.get(id)
    if not user:
        abort(404)

    user.active = 0
    db.session.commit()
    flash("Successfully deactive user {} {}!".format(user.first_name, user.last_name))
    return "ok"


@app.route("/activate/<int:id>", methods=["POST"])
@login_required
def active(id):

    user = User.query.get(id)
    if not user:
        abort(404)

    user.active = 1
    db.session.commit()
    flash("Successfully active user {} {}!".format(user.first_name, user.last_name))
    return "ok"


@app.route("/account")
@login_required
def account():
    return render_template("account.html")


@app.route("/edit_account", methods=["POST", "GET"])
@login_required
def edit_my_account():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email_address")
        password = request.form.get("password")
        username = request.form.get("username")
        department = request.form.get("department")
        flash("Successfully save your information!")
        return redirect("account")

    return render_template("edit_my_account.html")