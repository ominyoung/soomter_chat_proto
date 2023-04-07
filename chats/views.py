from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from .serializers import MessageSerializers
from rest_framework.response import Response
from .models import Message


class MessageAPIView(RetrieveAPIView):
    """
        API URL : GET v1/message/{pk}
        Message API View
    """
    queryset = Message.objects.all()
    permission_classes = (AllowAny,)  # ToDo : 인증 구현후 IsAuthenticated 로변경
    serializer_class = MessageSerializers

    def retrieve(self, request, *args, **kwargs):
        """
            link 존재시 link 객체 Return
            존재 하지 않을시 depth += 1 객체들 Return
        """
        instance = self.get_object()
        if instance.depth in (5, 7, 9, 11):
            return Response({"detail:마지막 질문 입니다."}, status=status.HTTP_204_NO_CONTENT)
        if instance.link is not None:
            serializer = self.get_serializer(self.queryset.get(pk=instance.link))
        else:
            serializer = self.get_serializer(self.queryset.filter(depth=instance.depth + 1), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)