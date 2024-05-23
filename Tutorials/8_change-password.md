#### change password
- I remember old pass but I want to update it

1. user password change view --> views

2. user change password serializer --> serializer

3. set path

4. post method --> postman
    - add extra key inside the header
        - key: Authorization
        - value: Bearer access-token

    - we need access-token because of:
        - permission_classes = [IsAuthenticated] --> views
    
```
    {
        "password": "123456",
        "password2": "2024demo"
    }
```

5. Now try to login using new password