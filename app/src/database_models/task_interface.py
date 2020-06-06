from src.database_models.task_editor import TaskEditor

class TaskInterface:
    def set_changes(self, task_editor: TaskEditor) -> None:
        self.edit = task_editor

    def set_db(self, db) -> None:
        self.db = db

    def apply_changes(self):
        pass