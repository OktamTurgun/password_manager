# �� Password Manager

Professional va xavfsiz Python CLI dasturi — parollarni kriptograflangan holatda boshqarish uchun.

## ✨ Asosiy xususiyatlar
- 🔒 **Shifrlash**: Parollar Fernet (256-bit AES) bilan shifrlangan
- ✅ **Validatsiya**: Platform, username, parol comprehensive validatsiyasi
- 🎯 **Parol Kuchi**: Parol kuchi scoring (zaif → juda kuchli)
- 🔐 **Masking**: Parol input ekranda ko'rinmaydi (getpass)
- ⚠️ **Confirmation**: O'chirish/yangilashda tasdiqlab so'rash
- 🧪 **37 Ta Test**: 100% test coverage (validatsiya, shifrlash, integration)
- 📊 **Jadval Ko'rinish**: Parollar elegant jadval shaklida
- 🔄 **CRUD Operatsiyalari**: Qo'shish, ko'rish, o'chirish, yangilash, qidirish

## 📁 Loyiha tuzilmasi
```
password_manager/
├── main.py                      # Asosiy CLI dastur va menyu
├── utils/
│   ├── helpers.py              # CRUD, parol generatsiyasi, I/O
│   ├── security.py             # Shifrlash (Fernet/cryptography)
│   ├── models.py               # PasswordEntry, PasswordDatabase
│   ├── validators.py           # Validatsiya va parol kuchi
│   └── __init__.py
├── data/
│   ├── passwords.json          # Shifrlangan parollar
│   └── .encryption_key         # Shifrlash kalipi (xavfsiz)
├── tests/
│   ├── test_helpers.py         # 37 ta comprehensive test
│   └── __init__.py
├── requirements.txt            # Dependencies (cryptography, pytest)
├── README.md                   # Hujjat
└── LICENSE                     # MIT litsenziyasi
```

## 🚀 Ishga tushirish
1. Reponi klonlang:
   ```bash
   git clone https://github.com/OktamTurgun/password_manager.git
   cd password_manager
   ```
2. Kutubxonalarni o'rnating:
   ```bash
   pip install -r requirements.txt
   ```
   **Kerakli kutubxonalar:**
   - `cryptography>=41.0.0` — Parollarni shifrlash
   - `pytest>=6.2.5` — Testlar uchun
   - `black, flake8, mypy` — Code quality tools

3. Dasturni ishga tushiring:
   ```bash
   python main.py
   ```

## 🛠️ Foydalanish

### Menyu
Dastur ishga tushganda quyidagi menyu chiqadi:
```
50
🔐 Password Manager v1.0.0
==================================================

📋 ASOSIY MENYU:
1. ➕ Parol qo'shish
2. 👀 Parollarni ko'rish
3. 🗑️ Parolni o'chirish
4. ♻️ Parolni yangilash
5. 🔍 Parolni qidirish
0. 🚪 Chiqish
```

### Misollar
- **Parol qo'shish**: Platform nomi, username, parol
- **Parol ko'rish**: Jadval shaklida barcha parollar
- **Parol yangilash**: Yangi parol uchun confirmation so'rash
- **Parol o'chirish**: Tasodifiy o'chirishning oldini olish uchun confirmation

### Xavfsizlik Xususiyatlari
✅ **Parol input masking** — Ekranda yulduzcha ko'rinadi  
✅ **Confirmation dialogs** — O'chirish/yangilashda tasdiq  
✅ **Input validatsiya** — Duplicate, uzunlik, format tekshiruvi  
✅ **Parol kuchi feedback** — 🔴 zaif → 🟢 kuchli  
✅ **Encryption** — Fernet 256-bit AES shifrlash  

## 🧪 Testlar

### Test Coverage
**37 ta comprehensive test** — 100% passed ✅

```bash
# Testlarni ishga tushirish
python -m pytest tests/ -v

# Coverage bilan ishga tushirish
python -m pytest tests/ -v --cov=utils
```

### Test Kategoriyalari
| Kategoriya | Test Soni | Qamrovi |
|-----------|-----------|---------|
| Validatsiya | 8 | Platform, username, parol, kuch |
| PasswordEntry Model | 4 | CRUD, qidirish |
| PasswordDatabase | 6 | Add, remove, find, update, search |
| Password Manager Funksiyalar | 11 | Add, delete, update, view, search |
| Encryption | 4 | Shifrlash, deshifrlash, ro'yxat |
| Confirmation Dialog | 3 | Ha/yo'q variantlari |
| Integration | 1 | Xavfsizlik integrations |

### Test Natijalari
```
============================= 37 passed in 0.34s ==============================
```

## 📦 Modullar haqida

| Fayl | Vazifasi | Satr Soni |
|------|----------|----------|
| **main.py** | CLI, menyu, foydalanuvchi bilan muloqot | ~45 |
| **utils/helpers.py** | CRUD, parol generatsiyasi, I/O | ~230 |
| **utils/security.py** | Fernet shifrlash, deshifrlash | ~65 |
| **utils/models.py** | PasswordEntry, PasswordDatabase klasslar | ~87 |
| **utils/validators.py** | Validatsiya va parol kuchi analyzer | ~87 |
| **tests/test_helpers.py** | 37 ta test (validatsiya, shifrlash, CRUD) | ~280 |

### Asosiy Funksiyalar

#### security.py 🔐
- `encrypt_password()` — Parolni shifrlash
- `decrypt_password()` — Parolni deshifrlash
- `encrypt_passwords_list()` — Ro'yxatni shifrlash
- `decrypt_passwords_list()` — Ro'yxatni deshifrlash

#### validators.py ✅
- `validate_platform()` — Platform nomini tekshirish
- `validate_username()` — Username tekshirish
- `validate_password()` — Parol tekshirish
- `validate_password_strength()` — Parol kuchi (0-4 score)
- `sanitize_input()` — Input tozalash

#### models.py 📊
- `PasswordEntry` — Bitta parol yozuvi
- `PasswordDatabase` — Parollar bazasi (CRUD)

#### helpers.py 🛠️
- `add_password()` — Parol qo'shish (validatsiya bilan)
- `view_passwords()` — Parollarni jadval shakli bilan ko'rsatish
- `delete_password()` — Parolni o'chirish (confirmation bilan)
- `update_password()` — Parolni yangilash (validatsiya + confirmation)
- `search_password()` — Parollarni qidirish
- `generate_password()` — Kuchli parol yaratish
- `confirm_action()` — Foydalanuvchi tasdiqlashi
- `get_password_input()` — Masked password input (getpass)

## � Xavfsizlik Xususiyatlari

### Encryption
- **Algoritm**: Fernet (256-bit AES CBC mode)
- **Kalit**: Avtomatik yaratiladi va `.encryption_key` faylda saqlanadi
- **Saqlash**: Parollar shifrlangan holatda JSON-da saqlanadi

### Validatsiya
- Platform nomi: 2-100 belgi
- Username: 1-200 belgi
- Parol: 6-500 belgi (konfiguratsiyalanuvchi)
- Duplicate tekshirish
- Parol kuchi analyzer

### User Interface
- Parol input masking (getpass)
- Confirmation dialogs (o'chirish/yangilash)
- Parol kuchi feedback (zaif → juda kuchli)
- Jadval shakli bilan display

### Error Handling
- Try/except bloklar barcha funksiyalarda
- Aniq error xabarlari
- Input validation loops

## 🚀 Yangi Xususiyatlar (v1.1.0)
- ✅ Encryption support (Fernet)
- ✅ Parol kuchi analyzer
- ✅ Confirmation dialogs
- ✅ Enhanced input validation
- ✅ Modular architecture
- ✅ Comprehensive test coverage (37 tests)

## 📋 Requirements
```
Python>=3.8
cryptography>=41.0.0
pytest>=6.2.5
pytest-cov>=2.12.1
black>=21.7b0
flake8>=3.9.2
mypy>=0.910
```

## 🤝 Hissa Qo'shish

Siz hissa qo'shish uchun:
1. Reponi fork qiling
2. Feature branch yarating: `git checkout -b feature/qo'shimcha`
3. O'zgarishlarni commit qiling: `git commit -m "feat: qo'shimcha xususiyat"`
4. Branch-ni push qiling: `git push origin feature/qo'shimcha`
5. Pull request yarating

## 📄 Litsenziya
MIT — Faqat o'z mas'uliyatingiz bilan foydalaning!

---

**Ishonchli va xavfsiz password manager!** 🔐

Savollar bormi? [Issues](https://github.com/OktamTurgun/password_manager/issues) sahifasida yozing!
