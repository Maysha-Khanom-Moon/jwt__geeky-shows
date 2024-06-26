from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import *

from django.contrib.auth import authenticate
from account.renderers import UserRenderer

# create token manually
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    
    # def get(self, request, format=None):
    # post --> to registration
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        
        # if serializer.is_valid():
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            
            # Generate Token Manually
            token = get_tokens_for_user(user)
            return Response({'token': token, 'msg': 'Registration Successful'}, status=status.HTTP_201_CREATED)
        
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    # def get(self, request, format=None):
    
    # post --> to registration
    def post(self, request, *args, **kwargs):
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        serializer = UserLoginSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = authenticate(email=email, password=password)
            
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token': token, 'msg': 'Login Successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'non_field': ['Email or Password is not valid']}}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    

# access logged user data
class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# password change
class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    
    # we need access-token
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        serializer = UserChangePasswordSerializer(data=request.data, context={'user': request.user})
        
        if serializer.is_valid(raise_exception=True):
            
            password = serializer.validated_data.get('password')
            user = authenticate(password=password)
            
            user = serializer.update(request.user, serializer.validated_data)
            return Response({'msg': 'Password Change Successful'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

