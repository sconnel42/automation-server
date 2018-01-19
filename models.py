# A file that defines the tables in the database

from app_def import bcrypt, db, migrate

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    pw_hash = db.Column(db.String(120))

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.pw_hash = bcrypt.generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % (self.name)
