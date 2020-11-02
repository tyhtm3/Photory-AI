from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from .managers import CustomUserManager

from django.utils.translation import ugettext_lazy as _
# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    profile = models.CharField(max_length=1)
    nickname = models.CharField(max_length=100) 
    object = CustomUserManager()

    def __str__(self):
        return self.email