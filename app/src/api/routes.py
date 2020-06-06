from flask_restful import Api, Resource
from flask import Blueprint, jsonify, request, current_app
from src.models import sql_db, User
from flask_bcrypt import Bcrypt
from werkzeug.security import safe_str_cmp
import jwt
import datetime


api_blueprint = Blueprint('api', __name__)
bcrypt = Bcrypt()
api = Api(api_blueprint)

def generate_jwt(username, email):
    payload = {
        'sub': {
            'username': username,
            'email': email
        }
    }
    return str(jwt.encode(
        payload,
        current_app.config.get('SECRET_KEY'),
        algorithm='HS256'
    ), 'utf-8')

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
    }, status

class UserResource(Resource):
    def get(self):
        # sign in
        user_data = {
            'email': request.form.get('email'),
            'password': request.form.get('password')
        }
        searched_user = sql_db.get_user(user_data['email'])
        if searched_user:
            if bcrypt.check_password_hash(searched_user.password, user_data['password']):
                return json_response(200, 'OK', {
                    'user': {
                        'email': user_data['email']
                    },
                    'token': generate_jwt(searched_user.username, user_data['email'])
                })
        return json_response(401, 'Incorrect e-mail or password', {
            'user': {
                'email': user_data['email']
            }
        })

    def post(self):
        # registration
        user_data = {
            'username': request.form.get('username'),
            'email': request.form.get('email'),
            'password': request.form.get('password'),
            'repeat_password': request.form.get('repeat_password')
        }
        if not sql_db.get_user(user_data['email']):
            if safe_str_cmp(user_data['password'], user_data['repeat_password']):
                new_user = User(
                    username=user_data['username'],
                    email=user_data['email'],
                    password=str(bcrypt.generate_password_hash(user_data['password']), 'utf-8')
                )
                sql_db.add_user(new_user)
                response_user_data = {
                    'username': user_data['username'],
                    'email': user_data['email']
                }
                return json_response(
                    200,
                    'OK',
                    {
                        'user': response_user_data,
                        'token': generate_jwt(response_user_data['username'], response_user_data['email'])
                    }
                )
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
