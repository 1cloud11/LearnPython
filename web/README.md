# Сайт с новостями Python и прогнозом погоды

Программа находит показатели погоды в данный момент и собирает новости с сайта [Python.org](https://www.python.org/).

## Установка

Клонируйте репозиторий:

```
git clone https://github.com/1cloud11/LearnPython.git
```
Создайте виртуальное окружение

Установите зависимости

Создайте файл config.py и задайте в нем базовые переменные:
```
basedir = os.path.abspath(os.path.dirname(__file__))

WEATHER_API_KEY = api_key
WEATHER_DEFAULT_CITY = city,country
WEATHER_URL = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..',
                                                      'webapp.db')
```

Для запуска сервера на Windows используйте команду:
```
set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
```
Для запуска сервера на Linux используйте команду:
```
export FLASK_APP=webapp && export FLASK_ENV=development && flask run
```