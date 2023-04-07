from .models import Message
from rest_framework import serializers

class MessageSerializers(serializers.ModelSerializer):
    """
        Message Serializer
    """
    class Meta:
        model = Message
        fields = ('pk', 'sentence', )
        extra_kwargs = {
            'pk': {'read_only': True},
            'sentence': {'read_only': True},
        }