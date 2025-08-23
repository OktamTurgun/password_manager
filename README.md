
# �� Password Manager

Minimal, ixcham va professional Python CLI dasturi — parollarni xavfsiz boshqarish uchun.

## ✨ Asosiy xususiyatlar
- Parol qo‘shish, ko‘rish, o‘chirish, yangilash, qidirish (CRUD)
- Kuchli parol generatsiyasi
- Parollarni JSON faylga saqlash
- Testlar bilan mustahkamlangan
- Faqat kerakli va ixcham kod

## 📁 Loyiha tuzilmasi
```
password_manager/
├── main.py                # Asosiy CLI dastur
├── utils/
│   └── helpers.py         # CRUD va yordamchi funksiyalar
├── data/
│   └── passwords.json     # Parollar saqlanadigan fayl
├── tests/
│   └── test_helpers.py    # Testlar
├── requirements.txt       # (Agar kerak bo‘lsa)
└── README.md              # Hujjat
```

## 🚀 Ishga tushirish
1. Reponi klonlang:
   ```bash
   git clone <repo-url>
   cd password_manager
   ```
2. (Agar kerak bo‘lsa) kutubxonalarni o‘rnating:
   ```bash
   pip install -r requirements.txt
   ```
3. Dasturni ishga tushiring:
   ```bash
   python main.py
   ```

## 🛠️ Foydalanish
Dastur ishga tushganda quyidagi menyu chiqadi:
```
1. ➕ Parol qo'shish
2. 👀 Parollarni ko'rish
3. 🗑️ Parolni o'chirish
4. ♻️ Parolni yangilash
5. 🔍 Parolni qidirish
0. 🚪 Chiqish
```

## 🧪 Testlar
Testlarni ishga tushirish uchun:
```bash
python -m unittest tests/test_helpers.py
```
Barcha testlar mustaqil va izolyatsiyalangan.

## 📦 Fayllar haqida qisqacha
- **main.py** — CLI va foydalanuvchi bilan muloqot
- **utils/helpers.py** — CRUD, parol generatsiyasi, faylga yozish/o‘qish
- **data/passwords.json** — Parollar saqlanadi
- **tests/test_helpers.py** — CRUD va generator uchun testlar

## 📄 Litsenziya
MIT

---

**Minimal, ixcham va professional password manager loyihasi!**
