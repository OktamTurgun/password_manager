# 🐳 Password Manager Dockerfile

FROM python:3.9-slim

# Ish papkasini belgilash
WORKDIR /app

# Metadata
LABEL maintainer="Password Manager Team"
LABEL version="1.0.0"
LABEL description="Xavfsiz parol boshqaruv dasturi"

# Tizim paketlarini yangilash va kerakli paketlarni o'rnatish
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Python kutubxonalarini nusxalash va o'rnatish
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Dastur fayllarini nusxalash
COPY . .

# Ma'lumotlar papkasini yaratish
RUN mkdir -p data

# Port ochish (agar kerak bo'lsa)
# EXPOSE 8000

# Dasturni ishga tushirish
CMD ["python", "main_enhanced.py"] 