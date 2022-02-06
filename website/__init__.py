from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path

dataBase = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    """ base function for creating site"""

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kevinwasntmutedlol'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    dataBase.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Cardpost

    
    create_db(app)

    return app

def create_db(application):
    """ check to make sure the database exists. create if it is not."""
    if not path.exists('website/' + DB_NAME):
        dataBase.create_all(app=application)
        print('Database created')