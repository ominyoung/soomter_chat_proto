from django.contrib import admin
from .models import IntroChat

@admin.register(IntroChat)
class IntroChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'sentence', 'depth', 'link']
