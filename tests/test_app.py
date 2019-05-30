import unittest
import os
import json
from . import post_json
from app import create_app, db


class FastfoodTestCase(unittest.TestCase):
    """This class represents the Fast Food test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.user = {'email': 'you@example.com', 'password': 'pass124123'}

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_user_createion(self):
        """Test API can create user (POST request)"""
        res = post_json(self.client, '/auth/register', self.user)
        self.assertEqual(res.status_code, 201)

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()
