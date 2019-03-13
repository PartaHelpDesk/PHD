from app.models import User
from flask import render_template, redirect, url_for
from . import user_blueprint


@user_blueprint.route('/')
def main():

    return redirect(url_for('user.login'))


@user_blueprint.route('/login')
def login():

    return render_template('login.html')


