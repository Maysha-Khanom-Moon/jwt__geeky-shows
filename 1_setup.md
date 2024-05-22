1. create virtual environment
    - python -m venv env

2. now activate env
    - cd env
    - cd Scripts
    - activate
    - cd ..
    - cd ..

3. install django
    - pip install django
    - check: pip freeze

4. create django project
    - django-admin startproject djangoAuthApi

5. create a django app inside the project
    - cd djangoAuthApi
    - python manage.py startapp account

6. add this app inside the project app
    - settings.py --> add inside the INSTALLED_APPS