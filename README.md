# Weather Forecast Project

Этот проект предназначен для получения прогноза погоды для любого города на ближайшие 7 дней. Проект использует Django для создания веб-приложения и API для получения данных о погоде.

## Используемые технологии

Django, requests, OpenCage Data API, Open Meteo API, JavaScript, jQuery, Docker, pytest.

## Установка и запуск

### Локальный запуск проекта:

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/radiant2958/Weather-Forecast-Project.git
    cd weather_project
    ```

2. Создайте и активируйте виртуальное окружение:

    ```bash
    python -m venv venv
    source venv/bin/activate  
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Выполните миграции базы данных:

    ```bash
    python manage.py migrate
    ```

5. Запустите сервер разработки:

    ```bash
    python manage.py runserver
    ```

### Запуск проекта с использованием Docker:

1. Соберите Docker образ:

    ```bash
    docker build -t weather_project .
    ```

2. Запустите контейнер:

    ```bash
    docker run -d -p 8000:8000 weather_project
    ```

Проект будет доступен по адресу `http://localhost:8000`.

### Запуск тестов с использованием pytest:

1. Убедитесь, что зависимости для тестирования установлены:

    ```bash
    pip install pytest
    ```

2. Запустите тесты:

    ```bash
    pytest
    ```

