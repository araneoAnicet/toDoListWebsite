class UserDatabaseInterface:
    def user_registration(self, username: str, email: str, password: str) -> None:
        pass

    def user_login(self, email: str, password: str) -> None:
        pass


class ProjectDatabaseInterface:
    def add_project(self, owner, name: str, description: str) -> None:
        pass

    def delete_project(self, owner, name: str) -> None:
        pass

    def add_task(self, project, task_name: str, task_description: str, task_priority: int) -> None:
        pass
