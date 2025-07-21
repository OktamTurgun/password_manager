# 📂 Dasturga yordamchi funksiyalar

import json
import os
import secrets
import string

DATA_FILE = "data/passwords.json"


def safe_input_password(prompt="Parol: "):
    return input(prompt)


def load_passwords(data_file=DATA_FILE):
    if not os.path.exists(data_file):
        return []
    with open(data_file, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except Exception:
            return []


def save_passwords(passwords, data_file=DATA_FILE):
    os.makedirs(os.path.dirname(data_file), exist_ok=True)
    with open(data_file, 'w', encoding='utf-8') as file:
        json.dump(passwords, file, indent=4, ensure_ascii=False)


def generate_password(length=12):
    if length < 8:
        raise ValueError("Parol uzunligi kamida 8 bo'lishi kerak!")
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}"
    password = [secrets.choice(chars) for _ in range(length)]
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)


def add_password(data_file=DATA_FILE):
    passwords = load_passwords(data_file)
    platform = input("Platforma nomi: ")
    username = input("Foydalanuvchi ismi: ")
    choice = input("Parolni o'zingiz kiritasizmi? (ha/yo'q): ").lower()
    if choice == 'ha':
        password = safe_input_password("Parol: ")
    else:
        password = generate_password()
        print(f"Avtomatik yaratilgan parol: {password}")
    passwords.append({
        "platform": platform,
        "username": username,
        "password": password
    })
    save_passwords(passwords, data_file)
    print("✅ Parol muvaffaqiyatli qo'shildi.")


def view_passwords(data_file=DATA_FILE):
    passwords = load_passwords(data_file)
    if not passwords:
        print("⚠️ Xozircha parollar yo'q.")
        return
    for p in passwords:
        print(f"{p['platform']} | {p['username']} | {p['password']}")


def delete_password(data_file=DATA_FILE):
    passwords = load_passwords(data_file)
    platform = input("Platforma: ")
    username = input("Foydalanuvchi ismi: ")
    new_passwords = [p for p in passwords if not (
        p['platform'] == platform and p['username'] == username)]
    save_passwords(new_passwords, data_file)
    print("✅ Parol o'chirildi (agar mavjud bo'lsa).")


def update_password(data_file=DATA_FILE):
    passwords = load_passwords(data_file)
    platform = input("Platforma: ")
    username = input("Foydalanuvchi ismi: ")
    updated = False
    for p in passwords:
        if p['platform'] == platform and p['username'] == username:
            p['password'] = safe_input_password("Yangi parol: ")
            updated = True
            break
    save_passwords(passwords, data_file)
    if updated:
        print("✅ Parol yangilandi.")
    else:
        print("❌ Parol topilmadi.")


def search_password(data_file=DATA_FILE):
    passwords = load_passwords(data_file)
    keyword = input("Qidirish so'zi (platforma yoki username): ").lower()
    results = [
        p for p in passwords
        if keyword in p['platform'].lower() or keyword in p['username'].lower()
    ]
    if not results:
        print("❌ Xech narsa topilmadi.")
    else:
        for p in results:
            print(f"{p['platform']} | {p['username']} | {p['password']}")
