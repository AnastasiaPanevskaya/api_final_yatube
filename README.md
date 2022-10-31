# Учебный проект API для модулей приложения YaTube
Учебный проект создавался для отработки материалов по **API**

Как запустить проект:

## Клонируем репозиторий и заходим в него через терминал
git clone git@github.com:AnastasiaPanevskaya/api_final_yatube.git
cd api_final_yatube

## Создать и запуспустить виртуальное окружение
python -m venv venv
source venv/Scripts/activate

## Установить зависимости 
pip install -r requirements.txt

## Выполните миграции
python manage.py migrate

## Запустить сервер 

python manage.py runserver

## Примеры запросов 
/api/v1/posts/ (GET)
/api/v1/posts/ (POST)
/api/v1/posts/{id}/ (PUT)
