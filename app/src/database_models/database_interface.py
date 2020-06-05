from flask_bcrypt import Bcrypt
import jwt


class UserDatabaseInterface:
    def set_bcrypt_object(self, bcrypt: Bcrypt) -> None:
        self.bcrypt = Bcrypt

    def set_user_class(self, user_class_ref):
        self.user_class_ref = user_class_ref

    def user_registration(self, username: str, email: str, password: str) -> None:
        pass

    def user_login(self, email: str, password: str) -> bool:
        pass

    def user_authentification(self, jwt_token: str) -> bool:
        pass


class ProjectDatabaseInterface:
    def set_project_class(self, project_class_ref):
        self.project_class_ref = project_class_ref

    def set_task_class(self, task_class_ref):
        self.task_class_ref = task_class_ref

    def add_project(self, owner, name: str, description: str) -> None:
        pass

    def delete_project(self, owner, name: str) -> None:
        pass

    def add_task(self, project, task_name: str, task_description: str, task_priority: int) -> None:
        pass
