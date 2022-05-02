from crypt import methods
from flask import Blueprint, render_template, redirect, url_for
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup():
    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    return 'Logout'

