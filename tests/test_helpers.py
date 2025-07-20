# 🧪 Helpers funksiyalari uchun testlar

import unittest
import os
import sys
from pathlib import Path
import time
from unittest.mock import patch

# Utils papkasini import qilish uchun
sys.path.append(str(Path(__file__).parent.parent))

# Helper funksiyalarni import qilish
try:
    from utils.helpers import (
        load_passwords,
        save_passwords,
        generate_password,
        search_password
    )
    HELPERS_AVAILABLE = True
except ImportError:
    print("⚠️ utils.helpers moduli topilmadi. Testlar o'tkazilmaydi.")
    HELPERS_AVAILABLE = False


class TestPasswordManager(unittest.TestCase):
    """Password manager funksiyalari uchun testlar"""

    def setUp(self):
        """Har bir test oldidan bajariladigan sozlamalar"""
        if not HELPERS_AVAILABLE:
            self.skipTest("Helpers moduli mavjud emas")

        # Temp fayl o'rniga oddiy fayl ishlatamiz
        self.test_file = "test_passwords.json"
        self.test_data = [
            {
                "platform": "Test Platform",
                "username": "test_user",
                "password": "test_password"
            }
        ]

    def tearDown(self):
        """Har bir testdan keyin bajariladigan tozalash"""
        # Test faylini o'chirish
        if os.path.exists(self.test_file):
            try:
                os.unlink(self.test_file)
            except PermissionError:
                # Agar fayl band bo'lsa, keyinroq o'chirishga harakat qilamiz
                time.sleep(0.1)
                try:
                    os.unlink(self.test_file)
                except Exception:
                    pass

    def test_generate_password_length(self):
        """Parol uzunligini tekshirish"""
        if not HELPERS_AVAILABLE:
            self.skipTest("Helpers moduli mavjud emas")

        password = generate_password(length=12)
        self.assertEqual(len(password), 12)

    def test_generate_password_minimum_length(self):
        """Minimal uzunlik chegarasini tekshirish"""
        if not HELPERS_AVAILABLE:
            self.skipTest("Helpers moduli mavjud emas")

        with self.assertRaises(ValueError):
            generate_password(length=5)

    def test_generate_password_contains_required_chars(self):
        """Parol kerakli belgilarni o'z ichiga olganini tekshirish"""
        if not HELPERS_AVAILABLE:
            self.skipTest("Helpers moduli mavjud emas")

        password = generate_password(length=12)

        # Katta harflar
        self.assertTrue(any(c.isupper() for c in password))
        # Kichik harflar
        self.assertTrue(any(c.islower() for c in password))
        # Raqamlar
        self.assertTrue(any(c.isdigit() for c in password))
        # Maxsus belgilar
        special_chars = "!@#$%^&*()_+-=[]{}"
        self.assertTrue(any(c in special_chars for c in password))

    def test_save_and_load_passwords(self):
        """Parollarni saqlash va yuklash funksiyalarini tekshirish"""
        if not HELPERS_AVAILABLE:
            self.skipTest("Helpers moduli mavjud emas")

        # Test ma'lumotlarini saqlash
        save_passwords(self.test_data)

        # Ma'lumotlarni yuklash
        loaded_data = load_passwords()

        # Natijalarni tekshirish
        self.assertEqual(loaded_data, self.test_data)

    def test_load_passwords_empty_file(self):
        """Bo'sh fayl uchun load_passwords funksiyasini tekshirish"""
        if not HELPERS_AVAILABLE:
            self.skipTest("Helpers moduli mavjud emas")

        # Bo'sh fayl yaratish
        data_file = Path("data/passwords.json")
        data_file.parent.mkdir(exist_ok=True)
        with open(data_file, 'w', encoding='utf-8') as f:
            f.write('[]')  # Bo'sh JSON array yozamiz

        result = load_passwords()
        self.assertEqual(result, [])

    def test_search_password_found(self):
        """Qidiruv funksiyasi - topilgan holat"""
        if not HELPERS_AVAILABLE:
            self.skipTest("Helpers moduli mavjud emas")

        with patch('builtins.input', return_value='Test'):
            with patch('utils.helpers.load_passwords', return_value=self.test_data):
                with patch('builtins.print') as mock_print:
                    search_password()
                    mock_print.assert_called()

    def test_search_password_not_found(self):
        """Qidiruv funksiyasi - topilmagan holat"""
        if not HELPERS_AVAILABLE:
            self.skipTest("Helpers moduli mavjud emas")

        with patch('builtins.input', return_value='Nonexistent'):
            with patch('utils.helpers.load_passwords', return_value=self.test_data):
                with patch('builtins.print') as mock_print:
                    search_password()
                    # "Xech narsa topilmadi" xabari chiqishi kerak
                    mock_print.assert_called_with("❌ Xech narsa topilmadi.")


class TestPasswordGeneration(unittest.TestCase):
    """Parol yaratish funksiyalari uchun testlar"""

    def test_password_length(self):
        """Parol uzunligini tekshirish"""
        try:
            from utils.encryption import generate_secure_password

            password = generate_secure_password(length=10)
            self.assertEqual(len(password), 10)
        except ImportError:
            self.skipTest("Encryption moduli mavjud emas")

    def test_password_complexity(self):
        """Parol murakkabligini tekshirish"""
        try:
            from utils.encryption import generate_secure_password

            password = generate_secure_password(length=12)

            # Har bir toifadan kamida 1 ta belgi
            self.assertTrue(any(c.isupper() for c in password))
            self.assertTrue(any(c.islower() for c in password))
            self.assertTrue(any(c.isdigit() for c in password))
            self.assertTrue(any(c in "!@#$%^&*()_+-=[]{}" for c in password))
        except ImportError:
            self.skipTest("Encryption moduli mavjud emas")


if __name__ == '__main__':
    unittest.main()
