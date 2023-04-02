from django.urls import path, include
from .views import IntroChatAPI

urlpatterns = [
    path("", IntroChatAPI.as_view())
]