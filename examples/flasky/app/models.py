from datetime import datetime

from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)

class Role(db.Model):
    __tablename__ = 'roles'
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)