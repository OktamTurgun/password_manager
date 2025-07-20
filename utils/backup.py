# 💾 Backup va Export funksiyalari

import json
import shutil
from datetime import datetime
from pathlib import Path
import zipfile
import csv

# Konfiguratsiya va helper funksiyalarni import qilish
try:
    from config import DATA_DIR, PASSWORDS_FILE, BACKUP_ENABLED, BACKUP_COUNT
except ImportError:
    # Agar config.py mavjud bo'lmasa, standart qiymatlar
    DATA_DIR = Path("data")
    PASSWORDS_FILE = DATA_DIR / "passwords.json"
    BACKUP_ENABLED = True
    BACKUP_COUNT = 5


def load_passwords():
    """Parollarni fayldan o'qish"""
    if not PASSWORDS_FILE.exists():
        return []
    try:
        with open(PASSWORDS_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception:
        return []


def save_passwords(passwords):
    """Parollarni faylga saqlash"""
    PASSWORDS_FILE.parent.mkdir(exist_ok=True)
    with open(PASSWORDS_FILE, 'w', encoding='utf-8') as file:
        json.dump(passwords, file, indent=4, ensure_ascii=False)


def create_backup():
    """Parollar faylini backup qilish"""
    if not BACKUP_ENABLED:
        return

    backup_dir = DATA_DIR / "backups"
    backup_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = backup_dir / f"passwords_backup_{timestamp}.json"

    try:
        if PASSWORDS_FILE.exists():
            shutil.copy2(PASSWORDS_FILE, backup_file)
            print(f"✅ Backup yaratildi: {backup_file}")

            # Eski backup'larni tozalash
            cleanup_old_backups(backup_dir)
        else:
            print("⚠️ Backup yaratish uchun fayl topilmadi")
    except Exception as e:
        print(f"❌ Backup yaratishda xatolik: {e}")


def cleanup_old_backups(backup_dir):
    """Eski backup fayllarini o'chirish"""
    backup_files = sorted(backup_dir.glob("passwords_backup_*.json"))

    if len(backup_files) > BACKUP_COUNT:
        files_to_delete = backup_files[:-BACKUP_COUNT]
        for file in files_to_delete:
            file.unlink()
            print(f"🗑️ Eski backup o'chirildi: {file.name}")


def export_to_csv(output_file="passwords_export.csv"):
    """Parollarni CSV formatda export qilish"""
    try:
        passwords = load_passwords()

        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['platform', 'username', 'password']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for password in passwords:
                writer.writerow(password)

        print(f"✅ Parollar CSV formatda export qilindi: {output_file}")
    except Exception as e:
        print(f"❌ Export qilishda xatolik: {e}")


def import_from_csv(csv_file):
    """CSV fayldan parollarni import qilish"""
    try:
        passwords = []

        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                passwords.append({
                    'platform': row['platform'],
                    'username': row['username'],
                    'password': row['password']
                })

        # Mavjud parollarga qo'shish
        existing_passwords = load_passwords()
        existing_passwords.extend(passwords)

        save_passwords(existing_passwords)
        print(f"✅ {len(passwords)} ta parol import qilindi")
    except Exception as e:
        print(f"❌ Import qilishda xatolik: {e}")


def export_to_zip(output_file="passwords_backup.zip"):
    """Parollar va backup'larni ZIP formatda export qilish"""
    try:
        with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Asosiy parollar fayli
            if PASSWORDS_FILE.exists():
                zipf.write(PASSWORDS_FILE, PASSWORDS_FILE.name)

            # Backup fayllari
            backup_dir = DATA_DIR / "backups"
            if backup_dir.exists():
                for backup_file in backup_dir.glob("*.json"):
                    zipf.write(backup_file, f"backups/{backup_file.name}")

        print(f"✅ ZIP backup yaratildi: {output_file}")
    except Exception as e:
        print(f"❌ ZIP yaratishda xatolik: {e}")
