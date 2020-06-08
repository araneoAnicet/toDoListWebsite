from flask_restful import Resource
from flask import request, current_app
from src.models import sql_db, User
from src.database_models.user_editor import UserEditor
from werkzeug.security import safe_str_cmp
from src.api.resources import bcrypt, generate_jwt, decode_jwt, json_response


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
                    'token': generate_jwt(searched_user.username, user_data['email']).decode('utf-8')
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
                    password=bcrypt.generate_password_hash(user_data['password'])
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
                        'token': generate_jwt(response_user_data['username'], response_user_data['email']).decode('utf-8')
                    }
                )
            return json_response(401, 'Passwords should be equal', None)
        return json_response(401, 'This user already exists!', None)

    def put(self):
        payload = decode_jwt(request.headers.get('token'))['sub']
        searched_user = sql_db.get_user(payload['email'])
        if searched_user:
            searched_user.set_db(sql_db)
            searched_user.set_changes(UserEditor(
                name=request.form.get('name'),
                email=request.form.get('email'),
                password=bcrypt.generate_password_hash(request.form.get('password'))
                ))
            searched_user.apply_changes()
            return json_response(200, 'OK', {
                'user': {
                    'before': {
                        'name': payload['name'],
                        'email': payload['email'],
                    },
                    'changes': {
                        'name': request.form.get('name'),
                        'email': request.form.get('email'),
                        'password_length': len(request.form.get('password'))
                    }
                }
            })
        return json_response(410, 'User does not exist', {
            'user': {
                'name': payload['name'],
                'email': payload['email']
            }
        })

    def delete(self):
        payload = decode_jwt(request.headers.get('token'))['sub']
        searched_user = sql_db.get_user(payload['email'])
        if searched_user:
            user_data = {
                'name': searched_user.username,
                'email': searched_user.email
            }
            sql_db.delete_user(searched_user)
            return json_response(200, 'OK', {
                'user': user_data
            })
        return json_response(410, 'User does not exist', {
            'user': {
                'name': payload['name'],
                'email': payload['email']
            }
        })