from django.contrib import admin
from .models import Message

@admin.register(Message)
class IntroChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'sentence', 'depth', 'link']
