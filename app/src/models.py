from flask_sqlalchemy import SQLAlchemy
from flask import current_app

sql_db = SQLAlchemy(current_app)

class User(sql_db.Model):
    id = sql_db.Column(sql_db.Integer, primary_key=True)
    username = sql_db.Column(sql_db.String(50), unique=False, nullable=False)
    email = sql_db.Column(sql_db.String(90), unique=True, nullable=False)
    password = sql_db.Column(sql_db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return f'User({self.id}::{self.username}::{self.email})'
