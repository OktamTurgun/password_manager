# 🔐 Xavfsizlik va shifrlash funksiyalari

from cryptography.fernet import Fernet
import os
import json

ENCRYPTION_KEY_FILE = "data/.encryption_key"
CIPHER_SUITE = None


def _get_or_create_key():
    """Shifrlash kalitini olish yoki yangi yaratish"""
    os.makedirs(os.path.dirname(ENCRYPTION_KEY_FILE), exist_ok=True)
    
    if os.path.exists(ENCRYPTION_KEY_FILE):
        with open(ENCRYPTION_KEY_FILE, 'rb') as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(ENCRYPTION_KEY_FILE, 'wb') as f:
            f.write(key)
        return key


def _initialize_cipher():
    """Cipher objekasini initsializatsiya qilish"""
    global CIPHER_SUITE
    if CIPHER_SUITE is None:
        key = _get_or_create_key()
        CIPHER_SUITE = Fernet(key)
    return CIPHER_SUITE


def encrypt_password(password: str) -> str:
    """Parolni shifrlash"""
    if not password:
        raise ValueError("Parol bo'sh bo'lishi mumkin emas!")
    
    cipher = _initialize_cipher()
    encrypted = cipher.encrypt(password.encode())
    return encrypted.decode()


def decrypt_password(encrypted_password: str) -> str:
    """Shifrlangan parolni deshifrlash"""
    try:
        cipher = _initialize_cipher()
        decrypted = cipher.decrypt(encrypted_password.encode())
        return decrypted.decode()
    except Exception as e:
        raise ValueError(f"Parolni deshifrlash muvaffaqiyatsiz: {e}")


def encrypt_passwords_list(passwords: list) -> list:
    """Parollar ro'yxatini shifrlash"""
    encrypted_list = []
    for p in passwords:
        encrypted_item = p.copy()
        encrypted_item['password'] = encrypt_password(p['password'])
        encrypted_list.append(encrypted_item)
    return encrypted_list


def decrypt_passwords_list(encrypted_list: list) -> list:
    """Shifrlangan parollar ro'yxatini deshifrlash"""
    decrypted_list = []
    for p in encrypted_list:
        decrypted_item = p.copy()
        decrypted_item['password'] = decrypt_password(p['password'])
        decrypted_list.append(decrypted_item)
    return decrypted_list
