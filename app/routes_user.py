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


@app.route('/user')
@login_required
def user():
    actives = get_active_users()
    inactives = get_inactive_users()
    return render_template('user.html', actives=actives, inactives=inactives)


@app.route('/add_user', methods=["POST", "GET"])
@login_required
def add_user():
    refresh = True
    if request.method == 'POST':
        
        dbm = DM.DatabaseMethods()
        username = request.form.get('username')
        first_name = request.form.get('first_name')
        last_name= request.form.get('last_name')
        email = request.form.get('email_address')
        level = request.form.get('user_level')

       #TODO Check if form is filled out, if not warn user
        
        result = dbm.CreateUserAccount(username, level, first_name, last_name, email)

        flash(result)

    return render_template('add_user.html')


@app.route("/edit_user/<int:id>", methods=["POST", "GET"])
@login_required
def edit_user(id):
    user = User.query.get(id)
    if not user:
        abort(404)
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get('email')
        print(first_name, last_name, email)
        if not first_name or not last_name or not email:
            flash('Incomplete user information. Please check!')
            return redirect(url_for('add_user'))

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        db.session.commit()
        flash("Successfully save user information!")
        return redirect(url_for("user"))
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


@app.route("/active/<int:id>", methods=["POST"])
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