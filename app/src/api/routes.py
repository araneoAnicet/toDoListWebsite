from flask_restful import Api, Resource
from flask import Blueprint, jsonify
from src.models import sql_db


api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)


class UserResource(Resource):
    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

    def post(self):
        pass


@api.route('/test')
def test():
    return jsonify({
        'message': 'Hello world!'
    })

api.add_resource(UserResource, '/user')
