from flask_restful import Api, Resource
from flask import Blueprint
from src.models import sql_db


api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)


class UserResource(Resource):
    def get(self):
        return {'message': 'Hello from REST API!'}

    def put(self):
        pass

    def delete(self):
        pass

    def post(self):
        pass

api.add_resource(UserResource, '/user')
