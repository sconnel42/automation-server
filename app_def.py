# A file to do the application initialization.

from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# App Definition
app = Flask(__name__)
app.config.update(
    PROPAGATE_EXCEPTIONS = True
)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

# Encrypt and set up database
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

# Create a session for the app to connect to the database
app.config['SQLALCHEMY_DATABASE_URI']
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=False)
sm = sessionmaker(bind=engine)
DBSession = scoped_session(sm)

__all__ = ['app', 'bcrypt', 'db', 'DBSession', 'migrate']
