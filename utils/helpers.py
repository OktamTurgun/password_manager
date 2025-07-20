# 📂 Dasturga yordamchi funksiyalar

import json
import os
import secrets
import string
from pathlib import Path
from getpass import getpass

# 📌 Parollar saqlanadigan fayl manzili
DATA_FILE = "data/passwords.json"


def load_passwords():
    """📖 JSON fayldan parollarni o'qib olish"""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        return json.load(file)


def save_passwords(passwords):
    """📝 Parollarni JSON faylga saqlash"""
    try:
        # 📌 papkani yaratish
        DATA_FILE.parent.mkdir(exist_ok=True)

        # 📌 ma'lumotlarni saqlash
        with open(DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(passwords, file, indent=4, ensure_ascii=False)

        print("✅ Parollar saqlandi")
    except Exception as e:
        print(f"❌ Xatolik: {e}")


def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    """
    🔒 Tartibli, xavfsiz va filtrlangan parol yaratadi.

    Parametrlar:
    - length: parol uzunligi (kamida 8 tavsiya)
    - use_upper: katta harflar ishlatilsinmi
    - use_lower: kichik harflar ishlatilsinmi
    - use_digits: raqamlar ishlatilsinmi
    - use_special: maxsus belgilar ishlatilsinmi

    Natija:
    - Uzunligi `length` bo'lgan, tasodifiy parol
    """
    if length < 8:
        raise ValueError("Parol uzunligi kamida 8 bo'lishi kerak!")

    # 📌 ishlatiladigan belgilar to'plamini tuzamiz
    char_sets = []
    if use_upper:
        char_sets.append(string.ascii_uppercase)
    if use_lower:
        char_sets.append(string.ascii_lowercase)
    if use_digits:
        char_sets.append(string.digits)
    if use_special:
        char_sets.append("!@#$%^&*()_+-=[]{}")

    # 📌 har bir toifadan belgi qo'shish
    password = []
    for char_set in char_sets:
        password.append(secrets.choice(char_set))

    # 📌 qolgan belgilarni to'ldirish
    all_chars = ''.join(char_sets)
    while len(password) < length:
        password.append(secrets.choice(all_chars))

    # 📌 belgilarni aralashtirish
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)


def add_password():
    """➕ Yangi parol qo'shish"""
    passwords = load_passwords()
    platform = input("Platforma nomi: ")
    username = input("Foydalanuvchi ismi: ")
    choice = input("Parolni o'zingiz kiritasizmi? (ha/yo'q): ").lower()

    if choice == 'ha':
        password = getpass("Parol: ")
    else:
        password = generate_password()
        print(f"Avtomatik yaratilgan parol: {password}")

    # 📌 yangi parolni roʻyxatga qoʻshish
    passwords.append({
        "platform": platform,
        "username": username,
        "password": password
    })

    save_passwords(passwords)
    print("✅ Parol muvaffaqiyatli qo'shildi.")


def view_passwords():
    """👀 Saqlangan parollarni ko'rish"""
    passwords = load_passwords()
    if not passwords:
        print("⚠️ Xozircha parollar yo'q.")
        return

    for p in passwords:
        print(f"{p['platform']} | {p['username']} | {p['password']}")


def delete_password():
    """🗑️ Parolni o'chirish"""
    passwords = load_passwords()
    platform = input("Platforma: ")
    username = input("Foydalanuvchi ismi: ")

    # 📌 berilgan platform va username ga mos kelmaydiganlarni qoldirib filtrlash
    passwords = [p for p in passwords if not (
        p['platform'] == platform and p['username'] == username)]

    save_passwords(passwords)
    print("✅ Parol o'chirildi (agar mavjud bo'lsa).")


def update_password():
    """♻️ Parolni yangilash"""
    passwords = load_passwords()
    platform = input("Platforma: ")
    username = input("Foydalanuvchi ismi: ")

    for p in passwords:
        if p['platform'] == platform and p['username'] == username:
            p['password'] = getpass("Yangi parol: ")
            break

    save_passwords(passwords)
    print("✅ Parol yangilandi.")


def search_password():
    """🔎 Parolni qidirish"""
    passwords = load_passwords()
    keyword = input("Qidirish so'zi (platforma yoki username): ").lower()

    # 📌 keyword platform yoki username ichida borlarini olish
    results = [
        p for p in passwords
        if keyword in p['platform'].lower() or keyword in p['username'].lower()
    ]

    if not results:
        print("❌ Xech narsa topilmadi.")
    else:
        for p in results:
            print(f"{p['platform']} | {p['username']} | {p['password']}")
