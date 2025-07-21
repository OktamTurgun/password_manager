# 🧪 Helpers funksiyalari uchun testlar

from utils.helpers import generate_password, save_passwords, load_passwords, add_password, view_passwords, delete_password, update_password, search_password
from unittest.mock import patch
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


class TestPasswordManager(unittest.TestCase):
    TEST_FILE = "data/test_passwords.json"

    def setUp(self):
        self.test_data = [{"platform": "Test Platform",
                           "username": "test_user", "password": "test_password"}]
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def tearDown(self):
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def test_generate_password_length(self):
        password = generate_password(length=12)
        self.assertEqual(len(password), 12)

    def test_generate_password_minimum_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=5)

    def test_generate_password_contains_required_chars(self):
        password = generate_password(length=12)
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in "!@#$%^&*()_+-=[]{}" for c in password))

    def test_save_and_load_passwords(self):
        save_passwords(self.test_data, data_file=self.TEST_FILE)
        loaded = load_passwords(data_file=self.TEST_FILE)
        self.assertEqual(loaded, self.test_data)

    def test_load_passwords_empty_file(self):
        with open(self.TEST_FILE, 'w', encoding='utf-8') as f:
            f.write('[]')
        result = load_passwords(data_file=self.TEST_FILE)
        self.assertEqual(result, [])

    def test_add_password(self):
        # Simulate user input for add_password
        with patch('builtins.input', side_effect=["PlatformA", "userA", "ha", "secretpass"]):
            add_password(data_file=self.TEST_FILE)
        loaded = load_passwords(data_file=self.TEST_FILE)
        self.assertEqual(loaded[0]['platform'], "PlatformA")
        self.assertEqual(loaded[0]['username'], "userA")
        self.assertEqual(loaded[0]['password'], "secretpass")

    def test_view_passwords(self):
        save_passwords(self.test_data, data_file=self.TEST_FILE)
        with patch('builtins.print') as mock_print:
            view_passwords(data_file=self.TEST_FILE)
            mock_print.assert_any_call(
                f"{self.test_data[0]['platform']} | {self.test_data[0]['username']} | {self.test_data[0]['password']}")

    def test_delete_password(self):
        save_passwords(self.test_data, data_file=self.TEST_FILE)
        with patch('builtins.input', side_effect=["Test Platform", "test_user"]):
            delete_password(data_file=self.TEST_FILE)
        loaded = load_passwords(data_file=self.TEST_FILE)
        self.assertEqual(loaded, [])

    def test_update_password(self):
        save_passwords(self.test_data, data_file=self.TEST_FILE)
        # Patch uchta input: platforma, username, yangi parol
        with patch('builtins.input', side_effect=["Test Platform", "test_user", "newpass"]):
            update_password(data_file=self.TEST_FILE)
        loaded = load_passwords(data_file=self.TEST_FILE)
        self.assertEqual(loaded[0]['password'], 'newpass')

    def test_search_password_found(self):
        save_passwords(self.test_data, data_file=self.TEST_FILE)
        with patch('builtins.input', return_value='Test'):
            with patch('builtins.print') as mock_print:
                search_password(data_file=self.TEST_FILE)
                mock_print.assert_called()

    def test_search_password_not_found(self):
        save_passwords(self.test_data, data_file=self.TEST_FILE)
        with patch('builtins.input', return_value='Nonexistent'):
            with patch('builtins.print') as mock_print:
                search_password(data_file=self.TEST_FILE)
                mock_print.assert_called_with("❌ Xech narsa topilmadi.")


if __name__ == '__main__':
    unittest.main()
