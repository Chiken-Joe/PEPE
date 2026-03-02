# PEPE


# Restful-Booker API Automation Tests

Автоматизированные тесты для API [Restful-Booker](https://restful-booker.herokuapp.com).  
Проект демонстрирует трёхуровневую архитектуру (клиенты, фикстуры, ассерты) и покрывает critical regression и regression сценарии.

## 📌 Особенности API, которые учтены в тестах

- **Сброс данных каждые 10 минут** — тесты не полагаются на предзагруженные записи, а динамически создают свои собственные.
- **Авторизация через Cookie** — после получения токена через `/auth` он автоматически добавляется в сессию клиента.
- **Предзагруженные 10 записей** — используются только в тестах фильтрации для проверки логики, но создаются и свои уникальные данные.
- **Специфические статусы** — например, `201 Created` для DELETE и `200 OK` для POST, что учтено в ожиданиях.

---

## 🧱 Структура проекта
restful-booker-tests/
├── README.md
├── requirements.txt
├── config.py
├── conftest.py
├── api/ # Слой работы с API (транспорт)
│ ├── init.py
│ ├── base_client.py # Базовый клиент с логированием
│ ├── auth_client.py # POST /auth
│ └── booking_client.py # Все методы для /booking
├── fixtures/ # Тестовые данные и фабрики
│ ├── init.py
│ └── booking_factory.py # Генерация payload'ов (valid, invalid, random)
├── asserts/ # Проверки (assertions)
│ ├── init.py
│ ├── response_asserts.py # Статус, Content-Type, наличие ключей, ошибки
│ └── booking_asserts.py # Сравнение броней, проверка типов
├── utils/
│ └── logger.py # Логирование запросов/ответов
└── tests/ # Автотесты
├── init.py
├── test_critical_regression.py # CR-тесты (P0)
└── test_regression.py # Регрессионные тесты (фильтры, негатив)



## 0. Требования

- Python 3.8 или выше
- pip

## 1. Установка

1. Клонировать репозиторий (или скопировать файлы проекта).
2. Перейти в корневую папку проекта:
   ```bash
   cd C:\Users\PC\IdeaProjects\Booking

## 2. Создайте и активируйте виртуальное окружение
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate


## 3. Установите зависимости
pip install -r requirements.txt


## 4. Запустите тест 
pytest tests/ -v
