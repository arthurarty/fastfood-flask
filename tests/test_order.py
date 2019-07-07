from . import post_json_header
from .base_test import BaseTest
from .sample_data.auth import admin_user, user_1
from .sample_data.orders import (create_order, menu_item_not_found,
                                 order_strings, incomplete_order)


class OrderTestCase(BaseTest):
    """This tests the order view"""
    def setUp(self):
        super().setUp()
        self.token = self.login_user(user_1)
        self.admin_token = self.login_admin_user(admin_user)

    def test_order_createion(self):
        """Test API can add menu (POST request)"""
        res = post_json_header(
            self.client, '/orders/', create_order(
                self.create_menu()), self.token)
        self.assertEqual(res.status_code, 201)
        self.assertIn(b'Order posted', res.data)

    def test_menu_not_found(self):
        """Test response when user orders item not on the menu"""
        res = post_json_header(
            self.client, '/orders/', menu_item_not_found, self.token)
        self.assertEqual(res.status_code, 404)
        self.assertIn(b'not found', res.data)

    def test_string_input(self):
        """Test api does not allow string input for order"""
        res = post_json_header(
            self.client, '/orders/', order_strings, self.token)
        self.assertEqual(res.status_code, 400)

    def test_incomplete_order(self):
        """Test orders input handles incomplete orders"""
        res = post_json_header(
            self.client, '/orders/', incomplete_order, self.token)
        self.assertEqual(res.status_code, 400)

    def test_return_orders(self):
        """Test orders endpoint returns orders when accessed by admin"""
        res = post_json_header(
            self.client, '/orders/', create_order(
                self.create_menu()), self.token)
        res = self.client().get(
            '/orders/', headers={
                'Authorization': 'Bearer ' + self.admin_token})
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'order_list', res.data)

    def test_unauthorized_access_orders(self):
        """Ensures /orders endpoint not accessable by users"""
        res = post_json_header(
            self.client, '/orders/', create_order(
                self.create_menu()), self.token)
        res = self.client().get(
            '/orders/', headers={'Authorization': 'Bearer ' + self.token})
        self.assertEqual(res.status_code, 401)
