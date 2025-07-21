# Asosiy main.py - Parollar boshqaruvchisining asosiy fayli

from utils.helpers import add_password, view_passwords, delete_password, update_password, search_password


def print_banner():
    print("=" * 50)
    print("🔐 Password Manager v1.0.0")
    print("=" * 50)


def print_menu():
    print("\n📋 ASOSIY MENYU:")
    print("1. ➕ Parol qo'shish")
    print("2. 👀 Parollarni ko'rish")
    print("3. 🗑️ Parolni o'chirish")
    print("4. ♻️ Parolni yangilash")
    print("5. 🔍 Parolni qidirish")
    print("0. 🚪 Chiqish")


def main():
    print_banner()
    while True:
        print_menu()
        choice = input("\n🔢 Tanlang (0-5 yoki 0): ")
        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            delete_password()
        elif choice == "4":
            update_password()
        elif choice == "5":
            search_password()
        elif choice == "0":
            print("\n👋 Dasturdan chiqildi!")
            break
        else:
            print("Noto'g'ri tanlov! 1-5 yoki 0 ni tanlang.")


if __name__ == "__main__":
    main()
