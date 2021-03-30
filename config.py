"""Flask Config - This File is NOT used"""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir,".env"))


class Config:
    """Base Config"""
    TESTING = True
    DEBUG = True
    FLASK_ENV = 'development'
    FLASK_APP = 'wsgi.py'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # database related
    SQLALCHEMY_DATABASE_URI= "sqlite:///topic_tool.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

# could add other classes defining dev/prod environments
# could use os.environ to look up local environment variables
# rather than expose them here - however, nothing is sacred so far.


