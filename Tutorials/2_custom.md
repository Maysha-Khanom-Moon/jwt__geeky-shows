#### Custom user model
1. go to account models.py
2. follow official (website)[https://docs.djangoproject.com/en/5.0/topics/auth/customizing/]
    - go to a full example

3. migrate
    - it will create a db.sqlite 

4. add custom user model inside the setting
    - AUTH_USER_MODEL = 'account.User'

5. to check custom user model
    - create a superuser --> python manage.py createsuperuser
        - admin@example.com
        - Admin
        - 1234


6. run server
    - /admin 
    - try to login

7. follow official website to make User Admin

8. FOREIGN KEY Constrain
    - it occurs when I try to change the email, or name or bla bla
    - because before AUTH_USER_MODEL declaration
    - so
        - stop server
        - delete trashe file(__pycache__)
        - delete 00xx_initial file
        - means we delete migration and db files

        - now make migrations again
        - create a superuser again