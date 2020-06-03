from flask_sqlalchemy import SQLAlchemy


sql_db = SQLAlchemy()

projects = sql_db.Table(
    sql_db.Column('project_id', sql_db.Integer, sql_db.ForeignKey('project.id'), primary_key=True),
    sql_db.Column('user_id', sql_db.Integer, sql_db.ForeignKey('user.id'), primary_key=True)
)


class User(sql_db.Model):
    id = sql_db.Column(sql_db.Integer, primary_key=True)
    username = sql_db.Column(sql_db.String(50), unique=False, nullable=False)
    email = sql_db.Column(sql_db.String(90), unique=True, nullable=False)
    password = sql_db.Column(sql_db.String(120), unique=False, nullable=False)
    owned_projects = sql_db.relationship('Project', backref='owner', lazy=True)
    member_projects = sql_db.relationship('Project', secondary=projects, lazy='subquery',
        backref=sql_db.backref('members', lazy=True))

    def __repr__(self):
        return f'User({self.id}::{self.username}::{self.email})'


class Project(sql_db.Model):
    id = sql_db.Column(sql_db.Integer, primary_key=True)
    name = sql_db.Column(sql_db.String(90), unique=False, nullable=True)
    description = sql_db.Column(sql_db.String(360), unique=False, nullable=True)
    owner_id = sql_db.Column(sql_db.Integer, sql_db.ForeignKey('owner.id'), nullable=False)
    tasts = sql_db.relationship('Task', backref='project', lazy=True)

    def __repr__(self):
        return f'Project({self.name}::{self.owner_id})'


class Task(sql_db.Model):
    id = sql_db.Column(sql_db.Integer, primary_key=True)
    name = sql_db.Column(sql_db.String(90), unique=True, nullable=False)
    description = sql_db.Column(sql_db.String(360), unique=False, nullable=True)
    priority = sql_db.Column(sql_db.Integer, unique=False, nullable=False)
    project_id = sql_db.Column(sql_db.Integer,
        sql_db.ForeignKey('project.id'), nullable=False)

    def __repr__(self):
        return f'Task({self.name}::{self.description})'
