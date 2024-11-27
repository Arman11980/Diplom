#Сравнение фреймворков Django и FastApi на приложении блог


##Содержание
  обзор проекта
  структура проекта
  Пример файловой структуры проекта
  Список необходимых библиотек
  заключение


##Обзор проекта

  Мною сделаны простые приложения(блог) для сравнения на базе фреймворков Django и FastAPI. Django предлагает множество встроенных функций, таких как ORM,
  система аутентификации, админ-панель и многое другое. FastAPI, в свою очередь, имеет меньше встроенных функций, что может потребовать дополнительных библиотек и компонентов.
  Django хорошо масштабируется для крупных проектов, что делает его подходящим для сложных веб-приложений,
  FastAPI, напротив, делает упор на скорость и простоту разработки, что делает его отличным выбором для создания высокопроизводительных API. 
  Поэтому сделаны приложения по разному, Django по больше, а FastAPI по меньше. Хотя принципиально выполняют одну и туже роль - блог.


##структура проекта

  домашняя страница Django
   Тут есть кнопки на добавления постов, чтение, удалене и коментариев к посту
   ![Снимок экрана 2024-11-26 220605](https://github.com/user-attachments/assets/8e36681e-030c-4e24-997e-d8b70b6a5637)

   панель администрирования
   ![Снимок экрана 2024-11-27 202405](https://github.com/user-attachments/assets/715cfca0-fc2a-48a8-96bb-d8a83a103bc3)
   ![Снимок экрана 2024-11-27 202457](https://github.com/user-attachments/assets/d890e302-45e2-4ccf-90ef-887e9ac10aee)
   ![Снимок экрана 2024-11-27 202729](https://github.com/user-attachments/assets/45f9602e-a140-4aa6-95d4-934621c5af44)

   домашняя страница FastAPI
     Простая страница с созданием поста

   ![Снимок экрана 2024-11-27 203919](https://github.com/user-attachments/assets/30b00082-e16f-4098-b1fe-644f1321392f)
   ![Снимок экрана 2024-11-27 204010](https://github.com/user-attachments/assets/661131b7-eeef-40c6-8fa3-adaca75d82e5)
   ![Снимок экрана 2024-11-27 204145](https://github.com/user-attachments/assets/4b38687d-a905-4ea0-a608-657e630cf692)

   
##Пример файловой структуры проекта для блога FastAPI

|-BlogFastAPI
  |-static
  |   |-style.css
  |-templates
  |    |-create_post.html
  |    |-index.html
  |    |-post.html
  |-main.py
  |-requirements.txt


##Пример файловой структуры проекта для блога Django
|-blog_site
  |-blogsite
    |-blog
    |   |-migrations
    |   |-__init__.py
    |   |-admin.py
    |   |-apps.py
    |   |-forms.py
    |   |-models.py
    |   |-tests.py
    |   |-views.py
    |-blogsite
    |   |-__init__.py
    |   |-asgi.py
    |   |-settings.py
    |   |-urls.py
    |   |-wsgi.py
    |-images
    |-media
    |   |-images
    |     |-images
    |-static
    |   |-style.css
    |-templates
    |   |-add_coment.html
    |   |-base.html
    |   |-delete.html
    |   |-home.html
    |   |-new_post.html
    |   |-reg_page.html
    |-db.sqlite3
    |-manage.py
    |-requirements.txt


##Список необходимых библиотек для блога Django

    asgiref==3.8.1
    Django==4.2.16
    django-bootstrap4==24.4
    sqlparse==0.5.1
    tzdata==2024.2


##Список необходимых библиотек для блога FastAPI

    annotated-types==0.7.0
    anyio==4.6.2.post1
    click==8.1.7
    colorama==0.4.6
    fastapi==0.115.5
    h11==0.14.0
    idna==3.10
    Jinja2==3.1.4
    MarkupSafe==3.0.2
    pydantic==2.9.2
    pydantic_core==2.23.4
    python-multipart==0.0.17
    sniffio==1.3.1
    starlette==0.41.2
    typing_extensions==4.12.2
    uvicorn==0.32.0


#Заключение

  Выбор фреймворка зависит от конкретных требований проекта и сложности задач.
  Django подходит для крупных проектов с большим количеством функций,
  а FastAPI — для создания высокопроизводительных API. Учитывая плюсы и минусы каждого фреймворка, можно сделать осознанный выбор,
  который удовлетворит потребности проекта и ускорит процесс разработки.
