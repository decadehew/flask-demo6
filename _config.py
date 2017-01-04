import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'demo6.db'
SECRET_KEY = 'myprecious'

DATABASE_PATH = os.path.join(basedir, DATABASE)

SQLALCHEMY_DATABASE_URI = 'sqlite:///'+DATABASE_PATH
SQLALCHEMY_TRACK_MODIFICATIONS = True
