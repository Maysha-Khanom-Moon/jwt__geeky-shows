from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import UserRegistrationSerializer

class UserRegistrationView(APIView):
    # def get(self, request, format=None):
    
    # post --> to registration
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg': 'Registration Successful'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)