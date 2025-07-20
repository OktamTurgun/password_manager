# 🔐 Xavfsizlik moduli

import base64
import hashlib
import os
import secrets
import string

# cryptography kutubxonasi mavjudligini tekshirish
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    CRYPTOGRAPHY_AVAILABLE = True
except ImportError:
    CRYPTOGRAPHY_AVAILABLE = False
    print("⚠️ cryptography kutubxonasi o'rnatilmagan. Oddiy shifrlash ishlatiladi.")


class PasswordEncryption:
    """Parollarni shifrlash va shifrdan chiqarish uchun klass"""

    def __init__(self, master_password):
        """Master parol asosida shifrlash kalitini yaratish"""
        self.master_password = master_password.encode()
        # Production'da random salt ishlatish kerak
        self.salt = b'password_manager_salt'

        if CRYPTOGRAPHY_AVAILABLE:
            self._generate_key_crypto()
        else:
            self._generate_key_simple()

    def _generate_key_crypto(self):
        """cryptography kutubxonasi bilan kalit yaratish"""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.master_password))
        self.cipher = Fernet(key)

    def _generate_key_simple(self):
        """Oddiy hash asosida kalit yaratish"""
        # Master paroldan kalit yaratish
        key_material = self.master_password + self.salt
        self.key = hashlib.sha256(key_material).digest()

    def encrypt_password(self, password):
        """Parolni shifrlash"""
        if CRYPTOGRAPHY_AVAILABLE:
            return self.cipher.encrypt(password.encode()).decode()
        else:
            # Oddiy XOR shifrlash (production uchun tavsiya etilmaydi)
            password_bytes = password.encode()
            encrypted = bytes(a ^ b for a, b in zip(
                password_bytes, self.key[:len(password_bytes)]))
            return base64.b64encode(encrypted).decode()

    def decrypt_password(self, encrypted_password):
        """Shifrlangan parolni ochish"""
        try:
            if CRYPTOGRAPHY_AVAILABLE:
                return self.cipher.decrypt(encrypted_password.encode()).decode()
            else:
                # Oddiy XOR shifrdan chiqarish
                encrypted_bytes = base64.b64decode(encrypted_password.encode())
                decrypted = bytes(a ^ b for a, b in zip(
                    encrypted_bytes, self.key[:len(encrypted_bytes)]))
                return decrypted.decode()
        except Exception as e:
            print(f"❌ Shifrdan chiqarishda xatolik: {e}")
            return None

    def verify_master_password(self, input_password):
        """Master parolni tekshirish"""
        return hashlib.sha256(input_password.encode()).hexdigest() == \
            hashlib.sha256(self.master_password).hexdigest()


class SimplePasswordManager:
    """Oddiy parol boshqaruvchisi (shifrlashsiz)"""

    def __init__(self):
        self.passwords = []

    def add_password(self, platform, username, password):
        """Parol qo'shish"""
        self.passwords.append({
            'platform': platform,
            'username': username,
            'password': password
        })

    def get_password(self, platform, username):
        """Parolni olish"""
        for pwd in self.passwords:
            if pwd['platform'] == platform and pwd['username'] == username:
                return pwd['password']
        return None

    def list_passwords(self):
        """Barcha parollarni ko'rsatish"""
        return self.passwords.copy()


def generate_secure_password(length=12):
    """Xavfsiz parol yaratish (standart kutubxonalar bilan)"""
    if length < 8:
        raise ValueError("Parol uzunligi kamida 8 bo'lishi kerak!")

    # Belgilar to'plami
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = "!@#$%^&*()_+-=[]{}"

    # Har bir toifadan kamida 1 ta belgi
    password = []
    password.append(secrets.choice(uppercase))
    password.append(secrets.choice(lowercase))
    password.append(secrets.choice(digits))
    password.append(secrets.choice(special))

    # Qolgan belgilarni to'ldirish
    all_chars = uppercase + lowercase + digits + special
    while len(password) < length:
        password.append(secrets.choice(all_chars))

    # Belgilarni aralashtirish
    password_list = list(password)
    secrets.SystemRandom().shuffle(password_list)

    return ''.join(password_list)
