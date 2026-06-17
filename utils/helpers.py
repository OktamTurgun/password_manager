# 📂 Dasturga yordamchi funksiyalar

import json
import os
import secrets
import string
import getpass
from utils.security import encrypt_password, decrypt_password, encrypt_passwords_list, decrypt_passwords_list
from utils.validators import (
    validate_platform, validate_username, validate_password,
    validate_password_strength, sanitize_input
)
from utils.models import PasswordEntry, PasswordDatabase

DATA_FILE = "data/passwords.json"


def get_password_input(prompt: str = "Parol: ") -> str:
    """Parolni masklaangan holatda qabul qilish (yulduzcha ko'rinadi)"""
    return getpass.getpass(prompt)


def load_passwords(data_file=DATA_FILE):
    if not os.path.exists(data_file):
        return []
    with open(data_file, 'r', encoding='utf-8') as file:
        try:
            encrypted_passwords = json.load(file)
            return decrypt_passwords_list(encrypted_passwords)
        except Exception:
            return []


def save_passwords(passwords, data_file=DATA_FILE):
    os.makedirs(os.path.dirname(data_file), exist_ok=True)
    encrypted_passwords = encrypt_passwords_list(passwords)
    with open(data_file, 'w', encoding='utf-8') as file:
        json.dump(encrypted_passwords, file, indent=4, ensure_ascii=False)


def generate_password(length=12):
    if length < 8:
        raise ValueError("Parol uzunligi kamida 8 bo'lishi kerak!")
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}"
    password = [secrets.choice(chars) for _ in range(length)]
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)


def add_password(data_file=DATA_FILE):
    try:
        passwords = load_passwords(data_file)
        
        # Platforma nomini olish va validatsiya qilish
        while True:
            platform = input("Platforma nomi: ")
            is_valid, error_msg = validate_platform(platform)
            if is_valid:
                break
            print(f"❌ {error_msg}")
        
        # Foydalanuvchi nomini olish va validatsiya qilish
        while True:
            username = input("Foydalanuvchi ismi: ")
            is_valid, error_msg = validate_username(username)
            if is_valid:
                break
            print(f"❌ {error_msg}")
        
        # Duplicate tekshirish
        for p in passwords:
            if p['platform'] == platform and p['username'] == username:
                print("❌ Bu platforma va foydalanuvchi kombinatsiyasi allaqachon mavjud!")
                return
        
        # Parol qo'shish usuli
        choice = input("Parolni o'zingiz kiritasizmi? (ha/yo'q): ").lower().strip()
        if choice in ['ha', 'h', 'yes', 'y']:
            while True:
                password = get_password_input("Parol: ")
                is_valid, error_msg = validate_password(password)
                if is_valid:
                    break
                print(f"❌ {error_msg}")
            
            # Parol kuchini ko'rsatish
            strength, strength_msg = validate_password_strength(password)
            print(f"Parol kuchi: {strength_msg}")
        else:
            password = generate_password()
            print(f"✅ Avtomatik yaratilgan parol: {password}")
        
        # Parolni saqlash
        passwords.append({
            "platform": platform,
            "username": username,
            "password": password
        })
        save_passwords(passwords, data_file)
        print("✅ Parol muvaffaqiyatli qo'shildi.")
    except Exception as e:
        print(f"❌ Xato: {str(e)}")


def view_passwords(data_file=DATA_FILE):
    try:
        passwords = load_passwords(data_file)
        if not passwords:
            print("⚠️  Xozircha parollar yo'q.")
            return
        
        # Jadval shakli bilan ko'rsatish
        print("\n" + "=" * 80)
        print(f"{'Platforma':<20} | {'Foydalanuvchi':<25} | {'Parol':<30}")
        print("=" * 80)
        
        for p in passwords:
            platform = p['platform'][:20]
            username = p['username'][:25]
            password = p['password'][:30]
            print(f"{platform:<20} | {username:<25} | {password:<30}")
        
        print("=" * 80 + "\n")
    except Exception as e:
        print(f"❌ Xato: {str(e)}")


def confirm_action(message: str = "Siz ishonchli musiz?") -> bool:
    """Foydalanuvchidan tasdiqlash so'rash"""
    response = input(f"\n⚠️  {message} (ha/yo'q): ").lower().strip()
    return response in ['ha', 'h', 'yes', 'y']


def delete_password(data_file=DATA_FILE):
    try:
        passwords = load_passwords(data_file)
        
        while True:
            platform = input("Platforma: ")
            is_valid, error_msg = validate_platform(platform)
            if is_valid:
                break
            print(f"❌ {error_msg}")
        
        while True:
            username = input("Foydalanuvchi ismi: ")
            is_valid, error_msg = validate_username(username)
            if is_valid:
                break
            print(f"❌ {error_msg}")
        
        # O'chirish uchun confirmation so'rash
        if not confirm_action(f"'{platform}' | '{username}' parolini o'chirib tashlamoqchisiz?"):
            print("❌ Amal bekor qilindi.")
            return
        
        initial_count = len(passwords)
        new_passwords = [p for p in passwords if not (
            p['platform'] == platform and p['username'] == username)]
        
        if len(new_passwords) < initial_count:
            save_passwords(new_passwords, data_file)
            print("✅ Parol o'chirildi.")
        else:
            print("❌ Parol topilmadi.")
    except Exception as e:
        print(f"❌ Xato: {str(e)}")


def update_password(data_file=DATA_FILE):
    try:
        passwords = load_passwords(data_file)
        
        while True:
            platform = input("Platforma: ")
            is_valid, error_msg = validate_platform(platform)
            if is_valid:
                break
            print(f"❌ {error_msg}")
        
        while True:
            username = input("Foydalanuvchi ismi: ")
            is_valid, error_msg = validate_username(username)
            if is_valid:
                break
            print(f"❌ {error_msg}")
        
        updated = False
        for p in passwords:
            if p['platform'] == platform and p['username'] == username:
                while True:
                    new_password = get_password_input("Yangi parol: ")
                    is_valid, error_msg = validate_password(new_password)
                    if is_valid:
                        break
                    print(f"❌ {error_msg}")
                
                # Parol kuchini ko'rsatish
                strength, strength_msg = validate_password_strength(new_password)
                print(f"Parol kuchi: {strength_msg}")
                
                # Yangilash uchun confirmation so'rash
                if not confirm_action("Parolni yangilashga rozisizmi?"):
                    print("❌ Amal bekor qilindi.")
                    return
                
                p['password'] = new_password
                updated = True
                break
        
        save_passwords(passwords, data_file)
        if updated:
            print("✅ Parol yangilandi.")
        else:
            print("❌ Parol topilmadi.")
    except Exception as e:
        print(f"❌ Xato: {str(e)}")


def search_password(data_file=DATA_FILE):
    try:
        passwords = load_passwords(data_file)
        keyword = input("Qidirish so'zi (platforma yoki username): ").lower().strip()
        
        if not keyword:
            print("❌ Qidirish so'zi bo'sh bo'lishi mumkin emas!")
            return []
        
        results = [
            p for p in passwords
            if keyword in p['platform'].lower() or keyword in p['username'].lower()
        ]
        
        if not results:
            print("❌ Xech narsa topilmadi.")
            return []
        
        # Jadval shakli bilan ko'rsatish
        print("\n" + "=" * 80)
        print(f"{'Platforma':<20} | {'Foydalanuvchi':<25} | {'Parol':<30}")
        print("=" * 80)
        
        for p in results:
            platform = p['platform'][:20]
            username = p['username'][:25]
            password = p['password'][:30]
            print(f"{platform:<20} | {username:<25} | {password:<30}")
        
        print("=" * 80 + "\n")
        return results
    except Exception as e:
        print(f"❌ Xato: {str(e)}")
        return []
