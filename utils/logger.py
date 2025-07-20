# 📝 Logging moduli

import logging
from pathlib import Path

# Konfiguratsiya sozlamalarini olish
try:
    from config import LOG_FILE, LOG_LEVEL, LOG_FORMAT
except ImportError:
    # Standart sozlamalar
    LOG_FILE = Path("data/password_manager.log")
    LOG_LEVEL = "INFO"
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"


def setup_logger():
    """Logging sozlamalarini o'rnatish"""
    # Log papkasini yaratish
    LOG_FILE.parent.mkdir(exist_ok=True)

    # Logger yaratish
    logger = logging.getLogger('password_manager')
    logger.setLevel(getattr(logging, LOG_LEVEL))

    # Handler mavjudligini tekshirish
    if not logger.handlers:
        # Faylga yozish uchun handler
        file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
        file_handler.setLevel(logging.INFO)

        # Format yaratish
        formatter = logging.Formatter(LOG_FORMAT)
        file_handler.setFormatter(formatter)

        # Handler'ni qo'shish
        logger.addHandler(file_handler)

    return logger


def log_action(action, details=None):
    """Amalni log qilish"""
    try:
        logger = setup_logger()
        message = f"Action: {action}"
        if details:
            message += f" | Details: {details}"
        logger.info(message)
    except Exception as e:
        print(f"❌ Log yozishda xatolik: {e}")


def log_error(error, context=None):
    """Xatoni log qilish"""
    try:
        logger = setup_logger()
        message = f"Error: {error}"
        if context:
            message += f" | Context: {context}"
        logger.error(message)
    except Exception as e:
        print(f"❌ Xatolik log qilishda xatolik: {e}")


def log_security_event(event, user=None):
    """Xavfsizlik hodisasini log qilish"""
    try:
        logger = setup_logger()
        message = f"Security Event: {event}"
        if user:
            message += f" | User: {user}"
        logger.warning(message)
    except Exception as e:
        print(f"❌ Xavfsizlik hodisasi log qilishda xatolik: {e}")


def get_log_file_path():
    """Log fayl manzilini qaytarish"""
    return LOG_FILE


def clear_logs():
    """Log faylini tozalash"""
    try:
        if LOG_FILE.exists():
            LOG_FILE.unlink()
            print("✅ Log fayli tozalandi")
        else:
            print("⚠️ Log fayli mavjud emas")
    except Exception as e:
        print(f"❌ Log tozalashda xatolik: {e}")
