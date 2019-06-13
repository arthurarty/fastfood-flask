import unittest

from app import create_app, db
from app.models.user import User

from . import get_token, post_json


class BaseTest(unittest.TestCase):
    """Base test class"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

        with self.app.app_context():
            # create all tables
            db.create_all()

    def register_user(self, user):
        """Register a user"""
        return post_json(self.client, '/auth/register', user)

    def login_user(self, user):
        """Login a user"""
        self.register_user(user)
        res = post_json(self.client, 'auth/login', user)
        return get_token(res)

    def make_admin(self, admin_email):
        with self.app.app_context():
            user_query = User.query.filter_by(email=admin_email).first()
            user_query.admin = True
            user_query.save()

    def login_admin_user(self, admin_user):
        """Login an admin user"""
        self.register_user(admin_user)
        email = admin_user['email']
        self.make_admin(email)
        res = post_json(self.client, 'auth/login', admin_user)
        return get_token(res)

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()
