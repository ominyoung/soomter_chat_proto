from django.urls import path
from .views import SignUpAPIView

urlpatterns = [
    path("register/", SignUpAPIView.as_view(), name='signup'),
]