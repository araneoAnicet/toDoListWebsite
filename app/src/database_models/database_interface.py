from flask_bcrypt import Bcrypt


class UserDatabaseInterface:
    def set_bcrypt_object(self, bcrypt: Bcrypt) -> None:
        self.bcrypt = Bcrypt

    def set_user_class(self, user_class_ref):
        self.user_class_ref = user_class_ref

    def user_registration(self, username: str, email: str, password: str, repeat_password: str) -> bool:
        pass

    def user_login(self, email: str, password: str) -> bool:
        pass

    def user_authentification(self, jwt_token: str) -> bool:
        pass

    def user_edit_name(self, user, new_name: str) -> bool:
        pass

    def user_edit_email(self, user, new_email: str) -> bool:
        pass

    def get_user(self, email: str):
        pass


class ProjectDatabaseInterface:
    def set_project_class(self, project_class_ref):
        self.project_class_ref = project_class_ref

    def set_task_class(self, task_class_ref):
        self.task_class_ref = task_class_ref

    def add_project(self, owner, name: str, description: str) -> None:
        pass

    def delete_project(self, project) -> None:
        pass

    def add_task(self, project, task_name: str, task_description: str, task_priority: int) -> None:
        pass

    def delete_task(self, task) -> None:
        pass

    def project_edit_name(self, project, new_name: str) -> bool:
        pass

    def project_edit_description(self, project, new_description: str) -> bool:
        pass

    def task_edit_name(self, task, new_name: str) -> bool:
        pass

    def task_edit_description(self, task, new_description: str) -> bool:
        pass

    def task_edit_priority(self, task, new_priority: str) -> bool:
        pass

    def get_project(self, owner, project_name: str):
        pass

    def get_task(self, project, task_name: str):
        pass
