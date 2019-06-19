from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from .utils import admin_required
from .models.order import Order
from .models.user import User
from psycopg2 import IntegrityError

bp = Blueprint('order', __name__, url_prefix='/orders')


@bp.route('/', methods=['POST'])
@jwt_required
def create_order():
    """Method to allow user make order"""
    request_data = request.get_json()
    input_fields = ['quantity', 'menu_id']
    input_data = {}
    for input_field in input_fields:
        try:
            if isinstance(request_data[input_field], int):
                input_data[input_field] = request_data[input_field]
            else:
                return jsonify(
                    error=f"{input_field} should be an integer"), 400
        except KeyError:
            return jsonify(message=f"{input_field} is missing"), 400
    current_user = get_jwt_identity()
    current_user_id = User.find(email=current_user)
    new_order = Order(input_data['quantity'])
    try:
        new_order.save(current_user_id, input_data['menu_id'])
    except IntegrityError:
        return jsonify(
            error=f"Menu item {input_data['menu_id']} not found"), 404
    return jsonify(message=f"Order posted"), 201
