from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserAPI(APIView):
    permission_classes = (AllowAny,)  # ToDo : 인증 구현후 IsAuthenticated 로변경

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)