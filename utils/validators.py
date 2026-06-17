# ✅ Validatsiya funksiyalari

import re
from typing import Tuple


def validate_platform(platform: str) -> Tuple[bool, str]:
    """Platforma nomini validatsiya qilish"""
    platform = platform.strip()
    if not platform:
        return False, "Platforma nomi bo'sh bo'lishi mumkin emas!"
    if len(platform) < 2:
        return False, "Platforma nomi kamida 2 ta belgi bo'lishi kerak!"
    if len(platform) > 100:
        return False, "Platforma nomi juda uzun (max 100 belgi)!"
    return True, ""


def validate_username(username: str) -> Tuple[bool, str]:
    """Foydalanuvchi nomini validatsiya qilish"""
    username = username.strip()
    if not username:
        return False, "Foydalanuvchi nomi bo'sh bo'lishi mumkin emas!"
    if len(username) < 1:
        return False, "Foydalanuvchi nomi kamida 1 ta belgi bo'lishi kerak!"
    if len(username) > 200:
        return False, "Foydalanuvchi nomi juda uzun (max 200 belgi)!"
    return True, ""


def validate_password(password: str, min_length: int = 6) -> Tuple[bool, str]:
    """Parolni validatsiya qilish"""
    if not password:
        return False, "Parol bo'sh bo'lishi mumkin emas!"
    if len(password) < min_length:
        return False, f"Parol kamida {min_length} ta belgi bo'lishi kerak!"
    if len(password) > 500:
        return False, "Parol juda uzun (max 500 belgi)!"
    return True, ""


def validate_password_strength(password: str) -> Tuple[int, str]:
    """
    Parol kuchini tekshirish
    Natija: (score, message)
    - score: 0-4 (0=zaif, 4=kuchli)
    """
    score = 0
    issues = []
    
    if len(password) >= 8:
        score += 1
    else:
        issues.append("Kamida 8 ta belgi qo'shish")
    
    if re.search(r'[a-z]', password):
        score += 1
    else:
        issues.append("Kichik harflar qo'shish")
    
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        issues.append("Katta harflar qo'shish")
    
    if re.search(r'[0-9!@#$%^&*()_+\-=\[\]{};:,.<>?]', password):
        score += 1
    else:
        issues.append("Raqamlar yoki maxsus belgilar qo'shish")
    
    messages = {
        0: "🔴 Parol juda zaif",
        1: "🟡 Parol zaif",
        2: "🟡 Parol o'rtacha",
        3: "🟢 Parol kuchli",
        4: "🟢 Parol juda kuchli"
    }
    
    message = messages[score]
    if issues:
        message += " (" + ", ".join(issues) + ")"
    
    return score, message


def sanitize_input(text: str) -> str:
    """Inputni tozalash (trim va basic xavfsizlik)"""
    return text.strip()[:500]  # Maksimal 500 belgi
