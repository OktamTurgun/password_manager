# 🔐 Password Manager - Enhanced Version

import os
import sys
from pathlib import Path
from utils.logger import setup_logger, log_action, log_error
from utils.backup import create_backup, export_to_csv, import_from_csv

# App sozlamalari
APP_NAME = "Password Manager"
APP_VERSION = "1.0.0"
DATA_DIR = Path("data")


def print_banner():
    """Dastur banner'ini ko'rsatish"""
    print("=" * 50)
    print(f"🔐 {APP_NAME} v{APP_VERSION}")
    print("=" * 50)


def print_menu():
    """Asosiy menyuni ko'rsatish"""
    print("\n📋 ASOSIY MENYU:")
    print("1. ➕ Parol qo'shish")
    print("2. 👀 Parollarni ko'rish")
    print("3. 🗑️ Parolni o'chirish")
    print("4. ♻️ Parolni yangilash")
    print("5. 🔍 Parolni qidirish")
    print("6. 💾 Backup yaratish")
    print("7. 📤 CSV export qilish")
    print("8. 📥 CSV import qilish")
    print("9. ⚙️ Sozlamalar")
    print("0. 🚪 Chiqish")


def backup_menu():
    """Backup menyusi"""
    print("\n💾 BACKUP MENYU:")
    print("1. Backup yaratish")
    print("2. CSV export qilish")
    print("3. CSV import qilish")
    print("0. Orqaga qaytish")

    choice = input("Tanlang: ")

    if choice == "1":
        create_backup()
        log_action("backup_created")
    elif choice == "2":
        filename = input(
            "Fayl nomi (default: passwords_export.csv): ") or "passwords_export.csv"
        export_to_csv(filename)
        log_action("csv_export", filename)
    elif choice == "3":
        filename = input("CSV fayl nomi: ")
        if os.path.exists(filename):
            import_from_csv(filename)
            log_action("csv_import", filename)
        else:
            print("❌ Fayl topilmadi!")
    elif choice == "0":
        return
    else:
        print("❌ Noto'g'ri tanlov!")


def settings_menu():
    """Sozlamalar menyusi"""
    print("\n⚙️ SOZLAMALAR:")
    print("1. Ma'lumotlar papkasini ochish")
    print("2. Log faylini ko'rish")
    print("3. Dastur haqida ma'lumot")
    print("0. Orqaga qaytish")

    choice = input("Tanlang: ")

    if choice == "1":
        try:
            if os.name == 'nt':
                os.startfile(DATA_DIR)
            else:
                # Xavfsizroq yo'l
                import subprocess
                subprocess.run(['xdg-open', str(DATA_DIR)], check=False)
            print("✅ Ma'lumotlar papkasi ochildi")
        except Exception:
            print("❌ Papka ochilmadi")
    elif choice == "2":
        log_file = DATA_DIR / "password_manager.log"
        if log_file.exists():
            with open(log_file, 'r', encoding='utf-8') as f:
                print("📝 LOG FAYLI:")
                print(f.read())
        else:
            print("⚠️ Log fayli hali yaratilmagan")
    elif choice == "3":
        print("\n📊 DASTUR HAQIDA:")
        print("Nomi: " + APP_NAME)
        print("Versiya: " + APP_VERSION)
        print("Ma'lumotlar papkasi: " + str(DATA_DIR))
        print("Python versiyasi: " + sys.version)
    elif choice == "0":
        return
    else:
        print("❌ Noto'g'ri tanlov!")


def handle_password_operations(choice):
    """Parol operatsiyalarini boshqarish"""
    operations = {
        "1": ("add_password", "password_added"),
        "2": ("view_passwords", "passwords_viewed"),
        "3": ("delete_password", "password_deleted"),
        "4": ("update_password", "password_updated"),
        "5": ("search_password", "password_searched")
    }

    if choice in operations:
        func_name, log_action_name = operations[choice]
        try:
            # Dinamik funksiya chaqirish
            globals()[func_name]()
            log_action(log_action_name)
        except (NameError, KeyError):
            print(f"❌ {func_name} funksiyasi mavjud emas")


def handle_menu_choice(choice):
    """Menyu tanlovini boshqarish"""
    if choice in ["1", "2", "3", "4", "5"]:
        handle_password_operations(choice)
    elif choice == "6":
        backup_menu()
    elif choice == "7":
        filename = input(
            "Fayl nomi (default: passwords_export.csv): ") or "passwords_export.csv"
        export_to_csv(filename)
        log_action("csv_export", filename)
    elif choice == "8":
        filename = input("CSV fayl nomi: ")
        if os.path.exists(filename):
            import_from_csv(filename)
            log_action("csv_import", filename)
        else:
            print("❌ Fayl topilmadi!")
    elif choice == "9":
        settings_menu()
    elif choice == "0":
        print("\n👋 Dasturdan chiqildi!")
        log_action("app_closed")
        return False
    else:
        print("❌ Noto'g'ri tanlov! 0-9 raqamlarini tanlang.")
    return True


def main():
    """Asosiy dastur funksiyasi"""
    # Logger'ni o'rnatish
    setup_logger()

    # Ma'lumotlar papkasini yaratish
    DATA_DIR.mkdir(exist_ok=True)

    # Banner'ni ko'rsatish
    print_banner()

    # Dastur ishga tushganini log qilish
    log_action("app_started")

    while True:
        try:
            print_menu()
            choice = input("\n🔢 Tanlang (0-9): ")

            if not handle_menu_choice(choice):
                break

        except KeyboardInterrupt:
            print("\n\n⚠️ Dastur to'xtatildi!")
            log_action("app_interrupted")
            break
        except Exception as e:
            print(f"❌ Xatolik yuz berdi: {e}")
            log_error(str(e), "main_loop")


if __name__ == "__main__":
    main()
