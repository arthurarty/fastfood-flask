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


@bp.route('/', methods=['GET'])
@jwt_required
def return_menu():
    """Return entire menu"""
    menu_items = Menu.query.all()
    entire_menu = []
    for menu_item in menu_items:
        obj = {
            'id': menu_item.id,
            'name': menu_item.name,
            'price': menu_item.price,
            'description': menu_item.description
        }
        entire_menu.append(obj)
    return jsonify(menu_items=entire_menu), 200


@bp.route('/<int:menu_id>/', methods=['GET'])
@jwt_required
def return_menu_item(menu_id):
    """Return single menu item of specified id"""
    menu_item = Menu.find(int(menu_id))
    menu_obj = {
        'id': menu_item.id,
        'name': menu_item.name,
        'price': menu_item.price,
        'description': menu_item.description
    }
    return jsonify(menu_item=menu_obj), 200
