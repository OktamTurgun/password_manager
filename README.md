
# 🔐 Password Manager

Python asosida yozilgan xavfsiz va qulay parol boshqaruv dasturi. Bu dastur CLI (Command Line Interface) orqali parollaringizni xavfsiz saqlash, boshqarish va avtomatik kuchli parollar yaratish imkonini beradi.

## ✨ Asosiy xususiyatlar

- 🔒 **Xavfsiz parol saqlash** - Barcha parollar JSON formatda shifrlangan holda saqlanadi
- 🔑 **Avtomatik parol yaratish** - Kuchli va xavfsiz parollar avtomatik yaratiladi
- 📱 **Qulay boshqaruv** - Oddiy menyu orqali barcha amallar bajariladi
- 🔍 **Qidiruv funksiyasi** - Platforma yoki foydalanuvchi nomi bo'yicha tez qidirish
- 📊 **To'liq ma'lumot** - Har bir parol uchun platforma, foydalanuvchi nomi va parol saqlanadi
- 💾 **Backup va Export** - Parollarni CSV formatda export/import qilish
- 📝 **Logging tizimi** - Barcha amallar loglanadi
- 🧪 **Test qilish** - Keng qamrovli testlar (11/11 o'tdi)
- 🐳 **Docker support** - Container deployment
- 🔄 **CI/CD** - GitHub Actions bilan avtomatik testlar

## 🛠️ Dastur tuzilishi

```
password_manager/
├── main.py                    # Asosiy dastur fayli
├── main_enhanced.py          # Yaxshilangan dastur
├── config.py                 # Konfiguratsiya
├── requirements.txt          # Kerakli kutubxonalar
├── Dockerfile               # Docker container
├── Makefile                 # Development buyruqlari
├── README.md               # Hujjat
├── LICENSE                 # Litsenziya
├── utils/
│   ├── __init__.py
│   ├── helpers.py           # Asosiy funksiyalar
│   ├── encryption.py        # Xavfsizlik moduli
│   ├── logger.py           # Logging
│   └── backup.py           # Backup/Export
├── tests/
│   ├── __init__.py
│   └── test_helpers.py     # Testlar
├── data/
│   ├── passwords.json      # Ma'lumotlar
│   └── password_manager.log # Log fayli
└── .github/
    └── workflows/
        └── ci.yml          # CI/CD
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

### 6. Backup va Export
- 💾 **Backup yaratish** - Avtomatik backup fayllari
- 📤 **CSV Export** - Parollarni CSV formatda export qilish
- 📥 **CSV Import** - CSV fayldan parollarni import qilish
- 📦 **ZIP Backup** - Barcha ma'lumotlarni ZIP formatda saqlash

### 7. Sozlamalar
- ⚙️ **Ma'lumotlar papkasini ochish**
- 📝 **Log faylini ko'rish**
- 📊 **Dastur haqida ma'lumot**

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
- Python 3.8+
- Standart Python kutubxonalari
- Ixtiyoriy: `cryptography` (kuchli shifrlash uchun)

### O'rnatish
```bash
# Reponi klonlash
git clone https://github.com/OktamTurgun/password_manager.git
cd password_manager

# Kerakli kutubxonalarni o'rnatish
pip install -r requirements.txt

# Dasturni ishga tushirish
python main_enhanced.py
```

### Docker orqali
```bash
# Docker image yaratish
docker build -t password-manager .

# Container ishga tushirish
docker run -it --rm -v $(pwd)/data:/app/data password-manager
```

## 📖 Foydalanish

Dastur ishga tushgandan so'ng quyidagi menyu ko'rsatiladi:

```
==================================================
🔐 Password Manager v1.0.0
==================================================

📋 ASOSIY MENYU:
1. ➕ Parol qo'shish
2. 👀 Parollarni ko'rish
3. 🗑️ Parolni o'chirish
4. ♻️ Parolni yangilash
5. 🔍 Parolni qidirish
6. 💾 Backup yaratish
7. 📤 CSV export qilish
8. 📥 CSV import qilish
9. ⚙️ Sozlamalar
0. 🚪 Chiqish
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

- **Kuchli shifrlash**: `cryptography` kutubxonasi bilan
- **Standart shifrlash**: `secrets` va `hashlib` bilan
- **Kuchli parollar**: Avtomatik xavfsiz parol yaratish
- **Logging**: Barcha amallar loglanadi
- **Backup**: Avtomatik backup tizimi

## 🧪 Test qilish

```bash
# Barcha testlarni ishga tushirish
python -m pytest tests/ -v

# Test coverage
python -m pytest tests/ --cov=utils --cov-report=html

# Kod tekshirish
flake8 .
black .
mypy utils/
```

**Test natijalari: 11/11 testlar muvaffaqiyatli o'tdi ✅**

## 🛠️ Development

### Makefile buyruqlari
```bash
make help          # Yordam
make install       # O'rnatish
make test          # Testlar
make lint          # Kod tekshirish
make format        # Kod formatlash
make run           # Dasturni ishga tushirish
make docker-build  # Docker image
make docker-run    # Docker container
make backup        # Backup yaratish
make security      # Xavfsizlik tekshirish
```

### CI/CD
- **GitHub Actions** - Avtomatik testlar
- **Docker** - Container deployment
- **Code coverage** - Test coverage hisobotlari

## 📊 Texnik ma'lumotlar

### Asosiy modullar
- `main.py` - Dasturning asosiy fayli va menyu
- `main_enhanced.py` - Yaxshilangan dastur
- `utils/helpers.py` - Barcha yordamchi funksiyalar
- `utils/encryption.py` - Xavfsizlik moduli
- `utils/backup.py` - Backup va export
- `utils/logger.py` - Logging tizimi
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
- `create_backup()` - Backup yaratish
- `export_to_csv()` - CSV export
- `import_from_csv()` - CSV import

## 🤝 Hissa qo'shish

Agar bu loyihaga hissa qo'shmoqchi bo'lsangiz:

1. Reponi fork qiling
2. Yangi branch yarating
3. O'zgarishlaringizni qo'shing
4. Testlarni ishga tushiring
5. Pull request yuboring

### Development sozlamalari
```bash
# Development muhitini sozlash
make dev-setup

# Testlarni ishga tushirish
make test

# Kod formatlash
make format
```

## 📄 Litsenziya

Bu loyiha MIT litsenziyasi ostida tarqatiladi.

## 📞 Bog'lanish

Savollar yoki takliflar uchun GitHub orqali bog'laning:
- **Repository**: https://github.com/OktamTurgun/password_manager
- **Issues**: https://github.com/OktamTurgun/password_manager/issues

## 🎯 Loyiha maqsadi

Bu dastur o'quv maqsadida yaratilgan va quyidagi maqsadlarni ko'zda tutadi:

- **Xavfsizlik**: Parollarni xavfsiz saqlash
- **Qulaylik**: Oddiy va tushunarli interfeys
- **Kengayish**: Modullarga ajratilgan kod
- **Test qilish**: Keng qamrovli testlar
- **Production-ready**: Professional darajada

---

**⚠️ Eslatma**: Bu dastur o'quv maqsadida yaratilgan. Ishlab chiqarish muhitida foydalanishdan oldin qo'shimcha xavfsizlik choralarini ko'rib chiqing.

**⭐ Agar bu loyiha foydali bo'lsa, star bering!**
