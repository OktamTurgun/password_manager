# 🛠️ Password Manager Makefile

.PHONY: help install test lint format clean run docker-build docker-run

# Default target
help:
	@echo "🔐 Password Manager - Yordamchi buyruqlar"
	@echo ""
	@echo "📋 Mavjud buyruqlar:"
	@echo "  install     - Kerakli kutubxonalarni o'rnatish"
	@echo "  test        - Testlarni ishga tushirish"
	@echo "  lint        - Kod tekshirish"
	@echo "  format      - Kod formatlash"
	@echo "  clean       - Vaqtinchalik fayllarni tozalash"
	@echo "  run         - Dasturni ishga tushirish"
	@echo "  docker-build - Docker image yaratish"
	@echo "  docker-run   - Docker container ishga tushirish"
	@echo "  backup      - Backup yaratish"
	@echo "  security    - Xavfsizlik tekshirish"

# O'rnatish
install:
	@echo "📦 Kerakli kutubxonalar o'rnatilmoqda..."
	pip install -r requirements.txt

# Testlar
test:
	@echo "🧪 Testlar ishga tushirilmoqda..."
	python -m pytest tests/ -v --cov=utils --cov-report=html

# Kod tekshirish
lint:
	@echo "🔍 Kod tekshirilmoqda..."
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
	mypy utils/ --ignore-missing-imports

# Kod formatlash
format:
	@echo "🎨 Kod formatlanmoqda..."
	black .
	isort .

# Tozalash
clean:
	@echo "🧹 Vaqtinchalik fayllar tozalanmoqda..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .coverage htmlcov/
	rm -rf build/ dist/
	rm -rf .pytest_cache/

# Dasturni ishga tushirish
run:
	@echo "🚀 Dastur ishga tushirilmoqda..."
	python main_enhanced.py

# Docker image yaratish
docker-build:
	@echo "🐳 Docker image yaratilmoqda..."
	docker build -t password-manager .

# Docker container ishga tushirish
docker-run:
	@echo "🐳 Docker container ishga tushirilmoqda..."
	docker run -it --rm -v $(PWD)/data:/app/data password-manager

# Backup yaratish
backup:
	@echo "💾 Backup yaratilmoqda..."
	python -c "from utils.backup import create_backup; create_backup()"

# Xavfsizlik tekshirish
security:
	@echo "🔒 Xavfsizlik tekshirilmoqda..."
	bandit -r . -f json -o bandit-report.json
	safety check

# Development setup
dev-setup: install
	@echo "🛠️ Development muhiti sozlanmoqda..."
	pre-commit install

# Production build
build: clean
	@echo "🏗️ Production build yaratilmoqda..."
	python setup.py sdist bdist_wheel

# Release
release: test lint security build
	@echo "�� Release tayyor!" 