from django.db import models
from django.contrib.auth.models import User
from apps.common.models import BaseModel

# Create your models here.

class UserProfile(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username