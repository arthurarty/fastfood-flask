from . import post_json_header
from .base_test import BaseTest
from .sample_data.auth import admin_user, user_1
from .sample_data.menus import menu_item, incomplete_menu


class MenuTestCase(BaseTest):
    """This tests the menu view"""
    def setUp(self):
        super().setUp()
        self.token = self.login_user(user_1)
        self.admin_token = self.login_admin_user(admin_user)

    def test_menu_createion(self):
        """Test API can add menu (POST request)"""
        res = post_json_header(
            self.client, '/menu/', menu_item, self.admin_token)
        self.assertEqual(res.status_code, 201)
        self.assertIn(b'Menu item', res.data)

    def test_incompete_data(self):
        """API should only create item if all data is provided"""
        res = post_json_header(
            self.client, '/menu/', incomplete_menu, self.admin_token)
        self.assertEqual(res.status_code, 400)

    def test_unauthorised_access(self):
        """Test if unauthorised user is not allowed to create menu"""
        res = post_json_header(
            self.client, '/menu/', menu_item, self.token)
        self.assertEqual(res.status_code, 401)
        self.assertIn(b'Unauthorized action', res.data)

    def test_get_menu(self):
        """Test API returns menu list"""
        res = post_json_header(
            self.client, '/menu/', menu_item, self.admin_token)
        res = self.client().get(
            '/menu/', headers={'Authorization': 'Bearer ' + self.token})
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'menu_items', res.data)
