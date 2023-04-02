from rest_framework import serializers
from .models import IntroChat

class IntroChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntroChat
        fields = ['sentence']