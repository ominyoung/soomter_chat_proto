from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class User(AbstractUser):
    """
        User Model
        기존 Base User Model 의 username, first_name, last_name 필드 삭제,
        email 필드에 Unique, 인증 수단 속성 부여
    """
    username = None
    first_name = None
    last_name = None

    nickname = models.CharField("Nickname", unique=True, max_length=80)
    email = models.EmailField(_('email address'), unique=True, help_text='Require', null=True)
    password = models.CharField(max_length=80)
    profile_image = models.ImageField(upload_to='user/%Y/%m/%d', null=True, blank=True)

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name_plural = "User DB"
        db_table = 'users'
