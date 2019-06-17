from . import post_json
from .base_test import BaseTest
from .sample_data import user_1, wrong_user_password


class AuthTestCase(BaseTest):
    """This class tests auth"""

    def test_user_createion(self):
        """Test API can create user (POST request)"""
        res = self.register_user(user_1)
        self.assertEqual(res.status_code, 201)
        self.assertIn(b'Registration Successful', res.data)

    def test_user_login(self):
        """Test API can login user (POST request)"""
        self.register_user(user_1)
        res = post_json(self.client, 'auth/login', user_1)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Login Successful', res.data)

    def test_wrong_password(self):
        """Test API can login user (POST request)"""
        self.register_user(user_1)
        res = post_json(self.client, 'auth/login', wrong_user_password)
        self.assertEqual(res.status_code, 401)
        self.assertIn(b'Wrong username or password', res.data)

    def test_login_unregistered_user(self):
        """Test API can login user (POST request)"""
        res = post_json(self.client, 'auth/login', wrong_user_password)
        self.assertEqual(res.status_code, 401)
        self.assertIn(b'Wrong username or password', res.data)
