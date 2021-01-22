from flask import Flask
from .routes import main
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session



def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretveryverysecret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SESSION_TYPE'] = 'sqlalchemy'
    

    db = SQLAlchemy(app)

    app.config['SESSION_SQLALCHEMY'] = db

    sess = Session(app)


    #db.create_all(app=app)

    app.config.from_pyfile(config_file)
    app.register_blueprint(main)

    return app
