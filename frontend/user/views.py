from frontend.models import User
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user, login_required
from . import user_blueprint


@user_blueprint.route('/')
def main():
    return redirect(url_for('user.login'))


@user_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if not user:
            flash('Login failed, user not found.')
            return redirect(url_for('user.login'))
        if not user.verify_password(password):
            flash('Login failed, your password seems wrong.')
            return redirect(url_for('user.login'))
        login_user(user)
        return redirect(url_for('main.dashboard'))
    return render_template('login.html')


@user_blueprint.route('/logout')
@login_required
def logout():
    login_user(current_user)
    return redirect(url_for('user.login'))
