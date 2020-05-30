from flask import Blueprint, jsonify

mod = Blueprint('api', __name__)

@mod.route('/')
def hello_wrold():
    return jsonify({
        'message': 'hello world!'
    })
