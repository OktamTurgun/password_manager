# ⚙️ Dastur konfiguratsiyasi

from pathlib import Path

# 📁 Asosiy papkalar
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
UTILS_DIR = BASE_DIR / "utils"
TESTS_DIR = BASE_DIR / "tests"

# 📄 Fayl manzillari
PASSWORDS_FILE = DATA_DIR / "passwords.json"
CONFIG_FILE = DATA_DIR / "config.json"
LOG_FILE = DATA_DIR / "password_manager.log"

# 🔐 Xavfsizlik sozlamalari
DEFAULT_PASSWORD_LENGTH = 12
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 50

# 📊 Dastur sozlamalari
APP_NAME = "Password Manager"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "Xavfsiz parol boshqaruv dasturi"

# 🎨 Ko'rsatish sozlamalari
MAX_DISPLAY_LENGTH = 50
PASSWORD_MASK = "********"

# 📝 Logging sozlamalari
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

# 🔧 Parol yaratish sozlamalari
PASSWORD_CHARS = {
    "uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "lowercase": "abcdefghijklmnopqrstuvwxyz",
    "digits": "0123456789",
    "special": "!@#$%^&*()_+-=[]{}|;:,.<>?"
}

# 📊 Ma'lumotlar bazasi sozlamalari
BACKUP_ENABLED = True
BACKUP_COUNT = 5
AUTO_SAVE = True
