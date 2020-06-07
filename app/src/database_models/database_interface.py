class DatabaseInterface:
    def set_class_references(self, user_class_ref, project_class_ref, task_class_ref) -> None:
        self.user_class_ref = user_class_ref
        self.project_class_ref = project_class_ref
        self.task_class_ref = task_class_ref

    def get_user(self, email: str):
        pass

    def add_user(self, user):
        pass

    def delete_user(self, user):
        pass

    def get_project(self, user, project_name: str):
        pass

    def add_project(self, user, project):
        pass

    def delete_project(self, project):
        pass

    def get_task(self, project, task_name: str):
        pass

    def add_task(self, project, task):
        pass

    def delete_task(self, task):
        pass