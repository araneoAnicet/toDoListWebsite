from src.database_models.project_editor import ProjectEditor

class ProjectInterface:
    def set_changes(self, project_editor: ProjectEditor) -> None:
        self.edit = project_editor

    def set_db(self, db) -> None:
        self.db = db

    def apply_changes(self):
        pass
