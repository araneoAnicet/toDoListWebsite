from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from src.models import sql_db, User, Project, Task
from flask import redirect, url_for
from flask import Blueprint


admin = Admin()
admin_blueprint = Blueprint('admin_blueprint', __name__)

admin.add_view(ModelView(User, sql_db.session))
admin.add_view(ModelView(Project, sql_db.session))
admin.add_view(ModelView(Task, sql_db.session))


@admin_blueprint.route('/')
def index():
    return redirect('/admin')