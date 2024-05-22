from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import UserRegistrationSerializer, UserLoginSerializer

from django.contrib.auth import authenticate

class UserRegistrationView(APIView):
    # def get(self, request, format=None):
    
    # post --> to registration
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg': 'Registration Successful'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    # def get(self, request, format=None):
    
    # post --> to registration
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = authenticate(email=email, password=password)
            
            if user is not None:
                return Response({'msg': 'Login Successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'non_field': ['Email or Password is not valid']}}, status=status.HTTP_401_UNAUTHORIZED)