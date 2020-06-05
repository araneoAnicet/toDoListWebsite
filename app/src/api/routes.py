from flask_restful import Api, Resource
from flask import Blueprint, jsonify, request
from src.models import sql_db, User
from flask_bcrypt import Bcrypt
from werkzeug.security import safe_str_cmp


api_blueprint = Blueprint('api', __name__)
bcrypt = Bcrypt()
api = Api(api_blueprint)

def json_response(status, message, data):
    return {
        'status': status,
        'message': message,
        'data': data,
        'payload': {
            'headers': dict(request.headers),
            'url': request.url,
            'method': request.method,
        }
    }

class UserResource(Resource):
    def get(self):
        pass

    def post(self):
        # registration
        user_data = {
            'username': request.form.get('username'),
            'email': request.form.get('email'),
            'password': request.form.get('password'),
            'repeat_password': request.form.get('repeat_password')
        }
        if not User.query.filter_by(email=user_data['email']).first():
            if safe_str_cmp(user_data['password'], user_data['repeat_password']):
                new_user = User(
                    username=user_data['username'],
                    email=user_data['email'],
                    password=str(bcrypt.generate_password_hash(user_data['password']), 'utf-8')
                )
                sql_db.session.add(new_user)
                sql_db.session.commit()
                response_user_data = {
                    'username': user_data['username'],
                    'email': user_data['email']
                }
                return json_response(200, 'OK', {'user': response_user_data})
            return json_response(401, 'Passwords should be equal', None)
        return json_response(401, 'This user already exists!', None)

    def put(self):
        pass

    def delete(self):
        pass


@api_blueprint.route('/test')
def test():
    return jsonify({
        'message': 'Hello world!'
    })

api.add_resource(UserResource, '/user')
