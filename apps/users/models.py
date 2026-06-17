from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from apps.users.managers import UserManager

# Create your models here.

class UserProfile(AbstractUser,PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    objects = UserManager()

    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return self.phone_number
    
