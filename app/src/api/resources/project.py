from flask_restful import Resource
from flask import request, current_app
from src.models import sql_db, Project
from src.database_models.project_editor import ProjectEditor
from werkzeug.security import safe_str_cmp
from src.api.resources import bcrypt, generate_jwt, decode_jwt, json_response


class ProjectResource(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
