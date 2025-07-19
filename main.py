# Asosiy main.py - Parollar boshqaruvchisining asosiy fayli

from utils.helpers import (
    add_password,
    view_passwords,
    delete_password,
    update_password,
    search_password
)


def menu():
    """
    Dastur menyusi.
    Foydalanuvchi tanlagan amalga qarab kerakli funksiyani chaqiradi.
    """
    while True:
        print("\n--- Password manager ---")
        print("1. Parol qo'shish")
        print("2. Parollarni ko'rish")
        print("3. Parolni o'chirish")
        print("4. Parolni yangilash")
        print("5. Parolni  qidirish")
        print("0. Chiqish")

        choice = input("Tanlang (1-5 yoki 0): ")

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
            print("\nDasturdan chiqildi!")
            break
        else:
            print("Noto'g'ri tanlov! 1-5 yoki 0 ni tanlang.")


if __name__ == "__main__":
    menu()
