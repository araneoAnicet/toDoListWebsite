from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from src.models import sql_db, User, Project, Task


admin = Admin()

admin.add_view(ModelView(User, sql_db.session))
admin.add_view(ModelView(Project, sql_db.session))
admin.add_view(ModelView(Task, sql_db.session))
