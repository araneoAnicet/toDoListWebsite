from src.database_models.user_editor import UserEditor

class UserInterface:
    def set_changes(self, user_editor: UserEditor) -> None:
        self.edit = user_editor

    def set_db(self, db) -> None:
        self.db = db

    def apply_changes(self):
        pass
