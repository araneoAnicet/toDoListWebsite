from flask_sqlalchemy import SQLAlchemy
from flask import current_app

sql_db = SQLAlchemy(current_app)

class User(sql_db.Model):
    id = sql_db.Column(sql_db.Integer, primary_key=True)
    username = sql_db.Column(sql_db.String(50), unique=False, nullable=False)
    email = sql_db.Column(sql_db.String(90), unique=True, nullable=False)
    password = sql_db.Column(sql_db.String(120), unique=False, nullable=False)
    owned_projects = sql_db.relationship('Project', backref='owner', lazy=True)

    def __repr__(self):
        return f'User({self.id}::{self.username}::{self.email})'


class Project(sql_db.Model):
    id = sql_db.Column(sql_db.Integer, primary_key=True)
    name = sql_db.Column(sql_db.String(90), unique=False, nullable=True)
    description = sql_db.Column(sql_db.String(360), unique=False, nullable=True)
    owner_id = sql_db.Column(sql_db.Integer, sql_db.ForeignKey('owner.id'), nullable=False)

    def __repr__(self):
        return f'Project({self.name}::{self.owner_id})'

