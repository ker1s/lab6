# E2E Test: SauceDemo Purchase
Этот проект содержит автоматизированный E2E-тест для проверки сценария покупки на сайте [saucedemo.com](https://www.saucedemo.com/).

## Требования
- Python 3.x
- Google Chrome

## Установка
### 1. Клонировать репозиторий
```bash
git clone https://github.com/ker1s/lab6.git
cd lab6
```

### 2. Создать и активировать виртуальное окружение
```bash
python3 -m venv .venv
.venv/bin/activate      # Linux/macOS
.venv\Scripts\activate.bat  # Windows cmd.exe
.venv\Scripts\Activate.ps1 # Windows PowerShell
```

### 3. Установить зависимости
```bash
pip install -r requirements.txt
```

## Запуск теста
# Запуск как скрипта
```bash
# Запуск как скрипта
python test_purchase.py

# Или через pytest
pytest -v test_purchase.py
```