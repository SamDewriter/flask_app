from crypt import methods
from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash, flash
from .models import User
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
    # code to validate and add user to the database
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    
    user = User.query.filter(email=email).first() # Check if the email already exists in the database
    
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    
    # Create a new user with the form and hash the password
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    
    # add the user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    return 'Logout'

