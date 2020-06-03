from flask_restful import API, Resource
from flask import current_app

api = API(current_app)

class UserResource(Resource):
    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

    def post(self):
        pass

api.add_resource(UserResource, '/user')