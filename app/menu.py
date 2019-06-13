from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from .utils import admin_required
from .models.menu import Menu

bp = Blueprint('menu', __name__, url_prefix='/menu')


@bp.route('/', methods=['POST'])
@jwt_required
@admin_required
def create():
    """Admin create menu item"""
    required_fields = ['price', 'name', 'description']
    request_data = request.get_json()
    menu_item = Menu()
    for required_field in required_fields:
        try:
            setattr(menu_item, required_field, request_data[required_field])
        except KeyError:
            return jsonify(message=f"{required_field} is missing"), 400
    menu_item.save()
    return jsonify(message=f"Menu item {menu_item.name} has been added"), 201
