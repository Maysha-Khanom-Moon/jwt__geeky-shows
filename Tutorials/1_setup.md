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


7. django rest framework setup
    - follow official website --> (drf)[https://www.django-rest-framework.org/]
    - check pip freeze


8. simple jwt token setup
    - follow official website --> (django simple jwt)[https://django-rest-framework-simplejwt.readthedocs.io/en/latest/]
    - check pip freeze

    - ##### works
        1. getting started:
            - only update 

        2. creating tokens manusally:
            - follow instructions
        
        3. settings:
            - ALGORITHM part delete
            - SLIDING_TOKEN part delete

            - just main 2 things is ACCESS_TOKEN_LIFETIME and REFRESH_TOKEN_LIFETIME
        

9. Fix CROS Policy Error
    - install django cors headers
        - follow (website)[https://pypi.org/project/django-cors-headers/]
        - cros middleware always before csrf