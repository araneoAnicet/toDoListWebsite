from flask_bcrypt import Bcrypt
from flask import current_app, request
import jwt

bcrypt = Bcrypt()

def generate_jwt(name, email):
    payload = {
        'sub': {
            'name': name,
            'email': email
        }
    }
    return jwt.encode(
        payload,
        current_app.config.get('SECRET_KEY'),
        algorithm='HS256'
    )

def decode_jwt(token):
    return jwt.decode(token, current_app.config.get('SECRET_KEY'), algorithm='HS256')

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
