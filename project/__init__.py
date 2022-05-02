from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

# init db so that it can be used later
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'my_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    
    db.init_app(app)
    
    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    # blueprint for non-auth part of the app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app
