# 🧪 Helpers funksiyalari uchun testlar

from utils.helpers import (
    generate_password, save_passwords, load_passwords, add_password, 
    view_passwords, delete_password, update_password, search_password,
    confirm_action, get_password_input
)
from utils.security import encrypt_password, decrypt_password, encrypt_passwords_list, decrypt_passwords_list
from utils.validators import (
    validate_platform, validate_username, validate_password,
    validate_password_strength, sanitize_input
)
from utils.models import PasswordEntry, PasswordDatabase
from unittest.mock import patch
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


class TestValidators(unittest.TestCase):
    """Validatsiya funksiyalarini test qilish"""
    
    def test_validate_platform_valid(self):
        is_valid, msg = validate_platform("Gmail")
        self.assertTrue(is_valid)
        self.assertEqual(msg, "")
    
    def test_validate_platform_empty(self):
        is_valid, msg = validate_platform("")
        self.assertFalse(is_valid)
        self.assertIn("bo'sh", msg)
    
    def test_validate_platform_too_short(self):
        is_valid, msg = validate_platform("A")
        self.assertFalse(is_valid)
    
    def test_validate_username_valid(self):
        is_valid, msg = validate_username("user@example.com")
        self.assertTrue(is_valid)
    
    def test_validate_password_valid(self):
        is_valid, msg = validate_password("SecurePass123!")
        self.assertTrue(is_valid)
    
    def test_validate_password_too_short(self):
        is_valid, msg = validate_password("123")
        self.assertFalse(is_valid)
    
    def test_password_strength_weak(self):
        score, msg = validate_password_strength("weak")
        self.assertEqual(score, 1)  # Uzunligi 4, faqat kichik harflar - 1 score
        self.assertIn("zaif", msg)
    
    def test_password_strength_strong(self):
        score, msg = validate_password_strength("StrongPass123!")
        self.assertGreaterEqual(score, 2)


class TestPasswordEntry(unittest.TestCase):
    """PasswordEntry modeli uchun testlar"""
    
    def test_password_entry_creation(self):
        entry = PasswordEntry("Gmail", "user@mail.com", "SecurePass123!")
        self.assertEqual(entry.platform, "Gmail")
        self.assertEqual(entry.username, "user@mail.com")
    
    def test_password_entry_to_dict(self):
        entry = PasswordEntry("Gmail", "user", "pass")
        data = entry.to_dict()
        self.assertEqual(data['platform'], "Gmail")
        self.assertEqual(data['username'], "user")
    
    def test_password_entry_from_dict(self):
        data = {"platform": "Gmail", "username": "user", "password": "pass"}
        entry = PasswordEntry.from_dict(data)
        self.assertEqual(entry.platform, "Gmail")
    
    def test_password_entry_search_match(self):
        entry = PasswordEntry("Gmail", "user@mail.com", "pass")
        self.assertTrue(entry.matches_search("gmail"))
        self.assertTrue(entry.matches_search("mail"))
        self.assertFalse(entry.matches_search("yahoo"))


class TestPasswordDatabase(unittest.TestCase):
    """PasswordDatabase modeli uchun testlar"""
    
    def setUp(self):
        self.db = PasswordDatabase()
        self.entry1 = PasswordEntry("Gmail", "user1", "pass1")
        self.entry2 = PasswordEntry("Yahoo", "user2", "pass2")
    
    def test_database_add(self):
        self.db.add(self.entry1)
        self.assertEqual(len(self.db.entries), 1)
    
    def test_database_find(self):
        self.db.add(self.entry1)
        found = self.db.find("Gmail", "user1")
        self.assertIsNotNone(found)
        self.assertEqual(found.password, "pass1")
    
    def test_database_find_not_found(self):
        found = self.db.find("Gmail", "user1")
        self.assertIsNone(found)
    
    def test_database_remove(self):
        self.db.add(self.entry1)
        removed = self.db.remove("Gmail", "user1")
        self.assertTrue(removed)
        self.assertEqual(len(self.db.entries), 0)
    
    def test_database_search(self):
        self.db.add(self.entry1)
        self.db.add(self.entry2)
        results = self.db.search("mail")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].platform, "Gmail")
    
    def test_database_update(self):
        self.db.add(self.entry1)
        updated = self.db.update("Gmail", "user1", "newpass")
        self.assertTrue(updated)
        found = self.db.find("Gmail", "user1")
        self.assertEqual(found.password, "newpass")


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
        with patch('builtins.input', side_effect=["PlatformA", "userA", "ha"]):
            with patch('utils.helpers.getpass.getpass', return_value="secretpass"):
                add_password(data_file=self.TEST_FILE)
        loaded = load_passwords(data_file=self.TEST_FILE)
        self.assertEqual(loaded[0]['platform'], "PlatformA")
        self.assertEqual(loaded[0]['username'], "userA")
        self.assertEqual(loaded[0]['password'], "secretpass")

    def test_view_passwords(self):
        save_passwords(self.test_data, data_file=self.TEST_FILE)
        with patch('builtins.print') as mock_print:
            view_passwords(data_file=self.TEST_FILE)
            # Jadval shaklida chop etiladi, shuning uchun platform nomi chop etilganligini tekshiramiz
            printed_output = str([call[0] for call in mock_print.call_args_list])
            self.assertIn("Test Platform", printed_output)

    def test_delete_password(self):
        save_passwords(self.test_data, data_file=self.TEST_FILE)
        with patch('builtins.input', side_effect=["Test Platform", "test_user", "ha"]):  # ha confirmation
            delete_password(data_file=self.TEST_FILE)
        loaded = load_passwords(data_file=self.TEST_FILE)
        self.assertEqual(loaded, [])

    def test_update_password(self):
        save_passwords(self.test_data, data_file=self.TEST_FILE)
        # Patch uchta input: platforma, username, va confirmation
        # Yangi parol getpass orqali
        with patch('builtins.input', side_effect=["Test Platform", "test_user", "ha"]):
            with patch('utils.helpers.getpass.getpass', return_value="newpass"):
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


class TestEncryption(unittest.TestCase):
    """Shifrlash funksiyalarini test qilish"""
    
    def test_encrypt_decrypt_password(self):
        password = "MySecurePassword123!"
        encrypted = encrypt_password(password)
        self.assertNotEqual(password, encrypted)
        decrypted = decrypt_password(encrypted)
        self.assertEqual(password, decrypted)
    
    def test_encrypt_empty_password(self):
        with self.assertRaises(ValueError):
            encrypt_password("")
    
    def test_encrypt_passwords_list(self):
        passwords = [
            {"platform": "A", "username": "user1", "password": "pass1"},
            {"platform": "B", "username": "user2", "password": "pass2"}
        ]
        encrypted = encrypt_passwords_list(passwords)
        # Shifrlangan parollar asl parollarga tengligi emas
        self.assertNotEqual(encrypted[0]['password'], "pass1")
        self.assertNotEqual(encrypted[1]['password'], "pass2")
        # Shifrlangan parollar turli (random nonce)
        self.assertNotEqual(encrypted[0]['password'], encrypted[1]['password'])
    
    def test_decrypt_passwords_list(self):
        passwords = [
            {"platform": "A", "username": "user1", "password": "pass1"}
        ]
        encrypted = encrypt_passwords_list(passwords)
        decrypted = decrypt_passwords_list(encrypted)
        self.assertEqual(decrypted[0]['password'], "pass1")


class TestConfirmationDialog(unittest.TestCase):
    """Confirmation dialog funksiyalarini test qilish"""
    
    def test_confirm_action_yes(self):
        with patch('builtins.input', return_value='ha'):
            result = confirm_action("Tasdiqlaysizmi?")
            self.assertTrue(result)
    
    def test_confirm_action_no(self):
        with patch('builtins.input', return_value='yo\'q'):
            result = confirm_action("Tasdiqlaysizmi?")
            self.assertFalse(result)
    
    def test_confirm_action_yes_variations(self):
        for response in ['ha', 'h', 'yes', 'y']:
            with patch('builtins.input', return_value=response):
                result = confirm_action()
                self.assertTrue(result)


class TestSecurityIntegration(unittest.TestCase):
    """Xavfsizlik integrations testlari"""
    
    def test_saved_passwords_are_encrypted(self):
        test_file = "data/test_secure_passwords.json"
        passwords = [
            {"platform": "TestApp", "username": "testuser", "password": "TestPassword123!"}
        ]
        
        try:
            # Parollarni saqlash
            save_passwords(passwords, test_file)
            
            # Fayl kontentini o'qish (parol shifrlangan bo'lishi kerak)
            with open(test_file, 'r') as f:
                content = f.read()
                # Parol shifrlangan, plain text ko'rinmaydi
                self.assertNotIn("TestPassword123!", content)
            
            # Parollarni yuklash (deshifrlangan bo'lishi kerak)
            loaded = load_passwords(test_file)
            self.assertEqual(loaded[0]['password'], "TestPassword123!")
            self.assertEqual(loaded[0]['username'], "testuser")
            self.assertEqual(loaded[0]['platform'], "TestApp")
        finally:
            if os.path.exists(test_file):
                os.remove(test_file)


if __name__ == '__main__':
    unittest.main()
