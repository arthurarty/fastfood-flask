import functools

from flask import (
    Blueprint, request, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
from .model import db, User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST'])
def register():
    request_data = request.get_json()
    email = request_data['email']
    password = request_data['password']
    user = User(email, password)
    user.save()
    return jsonify(email=user.email, message="User successfully registered")
