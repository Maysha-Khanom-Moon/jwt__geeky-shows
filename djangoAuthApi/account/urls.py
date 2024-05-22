from django.urls import path, include
from account.views import UserRegistrationView

urlpatterns = [
    # api/user/register/
    path('register/', UserRegistrationView.as_view(), name='register'),
]