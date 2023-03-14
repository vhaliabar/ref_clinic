""" creating Flask app using app factory pattern"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .extentions import db
from .rotes import main
#from med_ua.rest_api.api_rotes import api
#pylint: disable=wrong-import-order
#pylint: disable=wrong-import-position

def create_app(database_url='mysql+pymysql://root:password123@localhost/ref_clinic'):
    """ creating function that will construct the app """
    app = Flask(__name__)

    # Add database
    app.config['SQLALCHEMY_DATABASE_URI']=database_url
    app.config['SECRET_KEY']= 'very secret key'
    
    #MySQL config
    #database_url='mysql+pymysql://root:password123@localhost/ref_clinic'
    #SQLite config
    #'sqlite:///med_ua.sqlite3'

    # Initialize the database
    db.init_app(app)
    app.app_context().push()
    app.register_blueprint(main)
    #app.register_blueprint(api)
    return app

from ref_clinic import rotes #pylint: disable=wrong-import-order
#from ref_clinic.rest_api import api_rotes
from ref_clinic.rest_api import api_rotes_2 #pylint: disable=wrong-import-order


@main.cli.command('db_create')
def db_create():
    """ create cli command db_create """
    db.create_all()
    print('Database created!')


@main.cli.command('db_drop')
def db_drop():
    """ create cli command to delete db """
    db.drop_all()
    print('Database dropped!')
