import re

from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash, generate_password_hash

from .models.user import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST'])
def register():
    """Registering a new user"""
    request_data = request.get_json()
    email = request_data['email']
    reg = re.match(
        '([a-zA-Z0-9]+)([.]*)([-]*)([a-zA-Z0-9]+)@{1}([a-z]+)\.([a-z]+)',
        email)
    if reg is None:
        return jsonify(message="Invalid email address"), 401
    password = request_data['password']
    user = User(email, generate_password_hash(password))
    user.save()
    return jsonify(
        email=user.email, message="Registration Successful"
        ), 201


@bp.route('/login', methods=['POST'])
def login():
    """logging in an existing user"""
    request_data = request.get_json()
    email = request_data['email']
    password = request_data['password']
    user = User.query.filter_by(email=email).first()
    if (user is not None) and check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.email)
        return jsonify(
            message="Login Successful", token=access_token
            ), 200
    else:
        return jsonify(message="Wrong username or password"), 401
