from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import IntroChat
from .serializer import IntroChatSerializer

class IntroChatAPI(APIView):
    def get(self, request):
        
        result = IntroChat.objects.filter(depth=1)
        serializer = IntroChatSerializer(result, many=True)

        #field_1 = request.GET['field1']
        
        return Response(serializer.data, status=status.HTTP_200_OK)