Для запуска установите django:

pip install django

Также virtual env и requirements.txt:

pip install virtualenv

python -r requirements.txt

Сделайте миграции для создания базы данных:

python manage.py makemigrations

python manage.py migrate 

Создайте суперпользователя для взаимодействия админ-панелью:

python manage.py createsuperuser

ЗАПУСКАЙТЕ ПРОЕКТ:

cd blogsite

python manage.py runserver

