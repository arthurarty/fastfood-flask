from functools import wraps

from flask import jsonify
from flask_jwt_extended import get_jwt_identity

from .models.user import User


def admin_required(a_func):
    """Ensures only admin can use endpoint"""
    @wraps(a_func)
    def check_is_admin(*args, **kwargs):
        current_user_email = get_jwt_identity()
        user = User.query.filter_by(email=current_user_email).first()
        if user.admin:
            return a_func(*args, **kwargs)
        else:
            return jsonify(message="Unauthorized action"), 401
    return check_is_admin
