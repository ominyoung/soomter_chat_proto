from django.urls import path
from .views import MessageAPIView

urlpatterns = [
    path("message/<int:pk>/", MessageAPIView.as_view()),
]