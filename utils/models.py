# 📦 Password modeli va data klasslar

from typing import Optional
from dataclasses import dataclass


@dataclass
class PasswordEntry:
    """Parol yozuvi klassı"""
    platform: str
    username: str
    password: str
    
    def to_dict(self) -> dict:
        """Klassni lug'atga aylantirish"""
        return {
            "platform": self.platform,
            "username": self.username,
            "password": self.password
        }
    
    @staticmethod
    def from_dict(data: dict) -> 'PasswordEntry':
        """Lug'atdan klassni yaratish"""
        return PasswordEntry(
            platform=data.get("platform", ""),
            username=data.get("username", ""),
            password=data.get("password", "")
        )
    
    def matches_search(self, keyword: str) -> bool:
        """Qidiruv so'ziga mos kelishi"""
        keyword = keyword.lower()
        return (keyword in self.platform.lower() or 
                keyword in self.username.lower())


@dataclass
class PasswordDatabase:
    """Parollar bazasini boshqarish"""
    entries: list = None
    
    def __post_init__(self):
        if self.entries is None:
            self.entries = []
    
    def add(self, entry: PasswordEntry) -> bool:
        """Yangi parol qo'shish"""
        self.entries.append(entry)
        return True
    
    def remove(self, platform: str, username: str) -> bool:
        """Parolni o'chirish"""
        initial_count = len(self.entries)
        self.entries = [
            e for e in self.entries 
            if not (e.platform == platform and e.username == username)
        ]
        return len(self.entries) < initial_count
    
    def find(self, platform: str, username: str) -> Optional[PasswordEntry]:
        """Parol topish"""
        for e in self.entries:
            if e.platform == platform and e.username == username:
                return e
        return None
    
    def search(self, keyword: str) -> list:
        """Qidirish"""
        return [e for e in self.entries if e.matches_search(keyword)]
    
    def update(self, platform: str, username: str, new_password: str) -> bool:
        """Parolni yangilash"""
        entry = self.find(platform, username)
        if entry:
            entry.password = new_password
            return True
        return False
    
    def to_dict_list(self) -> list:
        """Ro'yxatni lug'atlar ro'yxatiga aylantirish"""
        return [e.to_dict() for e in self.entries]
    
    @staticmethod
    def from_dict_list(data: list) -> 'PasswordDatabase':
        """Lug'atlar ro'yxatidan Database yaratish"""
        db = PasswordDatabase()
        for item in data:
            db.add(PasswordEntry.from_dict(item))
        return db
