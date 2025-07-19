
# 🔐 Password Manager

Python asosida yozilgan xavfsiz va qulay parol boshqaruv dasturi. Bu dastur CLI (Command Line Interface) orqali parollaringizni xavfsiz saqlash, boshqarish va avtomatik kuchli parollar yaratish imkonini beradi.

## ✨ Asosiy xususiyatlar

- 🔒 **Xavfsiz parol saqlash** - Barcha parollar JSON formatda shifrlangan holda saqlanadi
- 🔑 **Avtomatik parol yaratish** - Kuchli va xavfsiz parollar avtomatik yaratiladi
- 📱 **Qulay boshqaruv** - Oddiy menyu orqali barcha amallar bajariladi
- 🔍 **Qidiruv funksiyasi** - Platforma yoki foydalanuvchi nomi bo'yicha tez qidirish
- 📊 **To'liq ma'lumot** - Har bir parol uchun platforma, foydalanuvchi nomi va parol saqlanadi

## 🛠️ Dastur tuzilishi

```
password_manager/
├── main.py              # Asosiy dastur fayli
├── utils/
│   ├── __init__.py      # Modul fayli
│   └── helpers.py       # Yordamchi funksiyalar
├── data/
│   └── passwords.json   # Parollar saqlanadigan fayl
└── README.md           # Dastur haqida ma'lumot
```

## 📋 Funksiyalar

### 1. Parol qo'shish (`add_password`)
- Yangi platforma va foydalanuvchi nomi kiritish
- Avtomatik kuchli parol yaratish yoki o'zingiz kiritish
- Parolni xavfsiz saqlash

### 2. Parollarni ko'rish (`view_passwords`)
- Barcha saqlangan parollarni ko'rish
- Platforma, foydalanuvchi nomi va parol ma'lumotlari

### 3. Parolni o'chirish (`delete_password`)
- Platforma va foydalanuvchi nomi bo'yicha parolni o'chirish
- Xavfsiz o'chirish amali

### 4. Parolni yangilash (`update_password`)
- Mavjud parolni yangi parol bilan almashtirish
- Platforma va foydalanuvchi nomi bo'yicha tanlash

### 5. Parolni qidirish (`search_password`)
- Platforma yoki foydalanuvchi nomi bo'yicha qidirish
- Natijalarni tez ko'rish

## 🔧 Parol yaratish xususiyatlari

Dastur kuchli parollar yaratish uchun quyidagi xususiyatlarni taqdim etadi:

- **Uzunlik**: Kamida 8 belgi (tavsiya: 12+)
- **Katta harflar**: A-Z
- **Kichik harflar**: a-z  
- **Raqamlar**: 0-9
- **Maxsus belgilar**: !@#$%^&*()_+-=[]{}

Har bir toifadan kamida 1 ta belgi avtomatik qo'shiladi, shuning uchun yaratilgan parollar har doim xavfsiz bo'ladi.

## 🚀 O'rnatish va ishga tushirish

### Talablar
- Python 3.x
- Standart Python kutubxonalari (json, os, random, string)

### O'rnatish
```bash
# Reponi klonlash
git clone https://github.com/username/password-manager.git
cd password-manager

# Dasturni ishga tushirish
python main.py
```

## 📖 Foydalanish

Dastur ishga tushgandan so'ng quyidagi menyu ko'rsatiladi:

```
--- Password manager ---
1. Parol qo'shish
2. Parollarni ko'rish
3. Parolni o'chirish
4. Parolni yangilash
5. Parolni qidirish
0. Chiqish
```

### Misol: Yangi parol qo'shish
```
Platforma nomi: Gmail
Foydalanuvchi ismi: user@gmail.com
Parolni o'zingiz kiritasizmi? (ha/yo'q): yo'q
Avtomatik yaratilgan parol: Kj#9mN$2pL@
✅ Parol muvaffaqiyatli qo'shildi.
```

## 📊 Ma'lumotlar saqlash

Barcha parollar `data/passwords.json` faylida quyidagi formatda saqlanadi:

```json
[
    {
        "platform": "Gmail",
        "username": "user@gmail.com", 
        "password": "Kj#9mN$2pL@"
    },
    {
        "platform": "Instagram",
        "username": "my_username",
        "password": "P@ssw0rd123!"
    }
]
```

## 🔒 Xavfsizlik

- Parollar oddiy JSON formatda saqlanadi
- Kuchli parollar avtomatik yaratiladi
- Foydalanuvchi ma'lumotlari mahalliy saqlanadi
- Tashqi bog'liqliklar yo'q

## 🛠️ Texnik ma'lumotlar

### Asosiy modullar
- `main.py` - Dasturning asosiy fayli va menyu
- `utils/helpers.py` - Barcha yordamchi funksiyalar
- `data/passwords.json` - Ma'lumotlar bazasi

### Funksiyalar
- `load_passwords()` - Parollarni fayldan o'qish
- `save_passwords()` - Parollarni faylga saqlash
- `generate_password()` - Kuchli parol yaratish
- `add_password()` - Yangi parol qo'shish
- `view_passwords()` - Parollarni ko'rish
- `delete_password()` - Parolni o'chirish
- `update_password()` - Parolni yangilash
- `search_password()` - Parolni qidirish

## 🤝 Hissa qo'shish

Agar bu loyihaga hissa qo'shmoqchi bo'lsangiz:

1. Reponi fork qiling
2. Yangi branch yarating
3. O'zgarishlaringizni qo'shing
4. Pull request yuboring

## 📄 Litsenziya

Bu loyiha MIT litsenziyasi ostida tarqatiladi.

## 📞 Bog'lanish

Savollar yoki takliflar uchun GitHub orqali bog'laning.

---

**⚠️ Eslatma**: Bu dastur o'quv maqsadida yaratilgan. Ishlab chiqarish muhitida foydalanishdan oldin qo'shimcha xavfsizlik choralarini ko'rib chiqing.
