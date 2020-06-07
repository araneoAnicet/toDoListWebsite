from flask_restful import Api, Resource
from flask import Blueprint, jsonify, request, current_app
from src.models import sql_db, User
from src.database_models.user_editor import UserEditor
from src.api.resources.user import UserResource
from flask_bcrypt import Bcrypt
from werkzeug.security import safe_str_cmp
import jwt



api_blueprint = Blueprint('api', __name__)

api = Api(api_blueprint)


@api_blueprint.route('/test')
def test():
    return jsonify({
        'message': 'Hello world!'
    })

api.add_resource(UserResource, '/user')
