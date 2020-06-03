from flask_restful import API, Resource
from flask import Blueprint
from src.models import sql_db


api_blueprint = Blueprint('api', __name__)
api = API(api_blueprint)

api.add_resource(UserResource, '/user')

class UserResource(Resource):
    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

    def post(self):
        pass
