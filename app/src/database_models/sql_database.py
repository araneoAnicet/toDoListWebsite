from src.database_models.database_interface import DatabaseInterface
from flask_sqlalchemy import SQLAlchemy


class SQLDatabase(SQLAlchemy, DatabaseInterface):
    def get_user(self, email: str):
        return self.user_class_ref.query.filter_by(email=email).first()

    def add_user(self, user):
        self.session.add(user)
        self.session.commit()

    def get_project(self, user, project_name: str):
        return user.query.join(
            user.owned_projects,
            alliased=True
            ).filter_by(name=project_name).first()
    
    def add_project(self, user, project):
        project.owner = user
        self.session.commit()

    def get_task(self, project, task_name: str):
        return project.query.join(
            project.tasks,
            alliased=True
        ).filter_by(name=task_name).first()

    def add_task(self, project, task):
        project.tasks.append(task)
        self.session.commit()