from frontend.models import User
from flask import render_template, redirect, url_for, request, flash
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
