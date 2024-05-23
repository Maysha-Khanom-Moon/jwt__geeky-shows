9. add User from admin panel
    - mkm1@example.com
    - moon1
    - 2024moon1

    - but moon1 user is not allowed to login from admin panel


10. registration panel for User --> api response
    - work on views
        - import Response, status, APIView from rest_framework
        - views map inside the urls

    - add urls --> account
    - then map this --> djangoAuthApi urls
    - copy-paste between two urls


11. to get as json
    - settings --> REST_FRAMEWORK:
        - 'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        )


12. but this defaul_render_classes we will not write inside the rest_framework.
    - we will create custom render_classes


13. post method
    - data pass to serializers

14. data method via postman
    - send a post request:
        {
            "email": "demo@example.com",
            "name": "Demo",
            "password": "2024demo",
            "password2": "2024demo",
            "tc": "True"
        }
