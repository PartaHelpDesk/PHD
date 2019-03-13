from app.models import User
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user
from . import user_blueprint


@user_blueprint.route('/')
def main():

    return redirect(url_for('user.login'))


@user_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if not user:
            flash('Login failed, user not found.')
            return redirect(url_for('login'))
        if not user.verify_password(password):
            flash('Login failed, your password seems wrong.')
    return render_template('login.html')


