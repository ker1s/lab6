# lab6
## Требования
- Python 3.x
- Google Chrome
- Учетная запись GitHub и персональный токен с правами `repo`.

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

# E2E Test: SauceDemo Purchase
Этот файл содержит автоматизированный E2E-тест для проверки сценария покупки на сайте [saucedemo.com](https://www.saucedemo.com/).
## Запуск теста
```bash
# Запуск как скрипта
python test_purchase.py

# Или через pytest
pytest -v test_purchase.py
```

# GitHub API Test
Файл автоматизированного теста для проверки работы с GitHub API: создание, проверка и удаление репозитория.

## Переменные окружения
Переименовать файл `.env` в `.env.example` или создать копию. 
Настроить в файле `.env` переменные следующим образом
GITHUB_USER=ваш_логин
GITHUB_TOKEN=ваш_токен
REPO_NAME=имя_тестового_репозитория

### Запуск теста
```bash
# Запуск скрипта напрямую
python test_github.py
```
```bash
# Запуск через pytest
pytest -v test_github.py
```