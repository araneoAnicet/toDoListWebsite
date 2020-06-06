from src.database_models.sql_database import SQLDatabase
from src.database_models.user_editor import UserEditor
from src.database_models.project_editor import ProjectEditor
from src.database_models.task_editor import TaskEditor
from src.database_models.user_interface import UserInterface
from src.database_models.project_interface import ProjectInterface
from src.database_models.task_interface import TaskInterface


sql_db = SQLDatabase()

projects = sql_db.Table(
    'projects',
    sql_db.Column('project_id', sql_db.Integer, sql_db.ForeignKey('project.id'), primary_key=True),
    sql_db.Column('user_id', sql_db.Integer, sql_db.ForeignKey('user.id'), primary_key=True)
)


class User(sql_db.Model, UserInterface):
    # sql database model
    id = sql_db.Column(sql_db.Integer, primary_key=True)
    username = sql_db.Column(sql_db.String(50), unique=False, nullable=False)
    email = sql_db.Column(sql_db.String(90), unique=True, nullable=False)
    password = sql_db.Column(sql_db.String(120), unique=False, nullable=False)
    owned_projects = sql_db.relationship('Project', backref='owner', lazy=True)
    member_projects = sql_db.relationship('Project', secondary=projects, lazy='subquery',
        backref=sql_db.backref('members', lazy=True))

    def apply_changes(self):
        new_name = self.edit.get_name()
        new_email = self.edit.get_email()
        new_password = self.edit.get_password()
        
        if new_name:
            self.username = new_name
        if new_email:
            self.email = new_email
        if new_password:
            self.password = new_password

        self.db.session.commit()

    def __repr__(self):
        return f'User({self.id}::{self.username}::{self.email})'


class Project(sql_db.Model, ProjectInterface):
    # sql database model
    id = sql_db.Column(sql_db.Integer, primary_key=True)
    name = sql_db.Column(sql_db.String(90), unique=False, nullable=False)
    description = sql_db.Column(sql_db.String(360), unique=False, nullable=True)
    owner_id = sql_db.Column(sql_db.Integer, sql_db.ForeignKey('user.id'), nullable=False)
    tasks = sql_db.relationship('Task', backref='project', lazy=True)

    def apply_changes(self):
        new_name = self.edit.get_name()
        new_description = self.edit.get_description()

        if new_name:
            self.name = new_name
        if new_description:
            self.description = new_description

        self.db.session.commit()

    def __repr__(self):
        return f'Project({self.name}::{self.owner_id})'


class Task(sql_db.Model):
    # sql database model
    id = sql_db.Column(sql_db.Integer, primary_key=True)
    name = sql_db.Column(sql_db.String(90), unique=True, nullable=False)
    description = sql_db.Column(sql_db.String(360), unique=False, nullable=True)
    priority = sql_db.Column(sql_db.Integer, unique=False, nullable=False)
    project_id = sql_db.Column(sql_db.Integer,
        sql_db.ForeignKey('project.id'), nullable=False)

    def apply_changes(self):
        new_name = self.edit.get_name()
        new_description = self.edit.get_description()
        new_priority = self.edit.get_priority()

        if new_name:
            self.name = new_name
        if new_description:
            self.description = new_description
        if new_priority:
            self.priority = new_priority

        self.db.session.commit()

    def __repr__(self):
        return f'Task({self.name}::{self.description})'
