from frontend.models import User, db
from flask import render_template, redirect, url_for, request, flash, abort
from flask_login import login_user, logout_user, current_user, login_required
from . import frontend
from frontend.utils import *


@frontend.route('/hliu32')
def main_2():
    return redirect(url_for('login_2'))


@frontend.route('/hliu32/login', methods=['POST', 'GET'])
def login_2():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if not user:
            flash('Login failed, user not found.')
            return redirect(url_for('login_2'))
        if not user.verify_password(password):
            flash('Login failed, your password seems wrong.')
            return redirect(url_for('login_2'))
        login_user(user)
        return redirect(url_for('dashboard_2'))
    return render_template('login.html')


@frontend.route('/hliu32/logout')
@login_required
def logout_2():
    login_user(current_user)
    return redirect(url_for('login_2'))


@frontend.route('/hliu32/user')
@login_required
def user_2():
    actives = get_active_users()
    inactives = get_inactive_users()
    return render_template('user.html', actives=actives, inactives=inactives)


@frontend.route('/hliu32/add_user', methods=["POST", "GET"])
@login_required
def add_user_2():

    if request.method == 'POST':
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        password = request.form.get('password')
        email = request.form.get('email')
        print(first_name, last_name, password, email)
        if not first_name or not last_name or not password or not email:
            flash('Incomplete user information. Please check!')
            return redirect(url_for(add_user_2))

        user = User(first_name=first_name, last_name=last_name, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        flash("Successfully create user {} {}!".format(user.first_name, user.last_name))
        return redirect(url_for("user_2"))
    return render_template('add_user.html')


@frontend.route("/hliu32/edit_user/<int:id>", methods=["POST", "GET"])
@login_required
def edit_user_2(id):
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
            return redirect(url_for(add_user_2))

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        db.session.commit()
        flash("Successfully save user information!")
        return redirect(url_for("user_2"))
    return render_template("edit_user.html", u=user)


@frontend.route("/hliu32/deactive/<int:id>", methods=["POST"])
@login_required
def deactive_2(id):

    user = User.query.get(id)
    if not user:
        abort(404)

    user.active = 0
    db.session.commit()
    flash("Successfully deactive user {} {}!".format(user.first_name, user.last_name))
    return "ok"


@frontend.route("/hliu32/active/<int:id>", methods=["POST"])
@login_required
def active_2(id):

    user = User.query.get(id)
    if not user:
        abort(404)

    user.active = 1
    db.session.commit()
    flash("Successfully active user {} {}!".format(user.first_name, user.last_name))
    return "ok"


@frontend.route("/hliu32/account")
@login_required
def account():

    return render_template("account.html")


@frontend.route("/hliu32/edit_account", methods=["POST", "GET"])
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
