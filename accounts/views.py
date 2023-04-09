from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from accounts.serializers import SignUpSerializer

class SignUpAPIView(CreateAPIView):
    serializer_class = SignUpSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                "message": "User created successfully",
                "data": serializer.data,
            }, status=status.HTTP_201_CREATED, headers=headers)
        return Response('잘못된 형식입니다.', status.HTTP_400_BAD_REQUEST)