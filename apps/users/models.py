from django.db import models
from apps.common.models import BaseModel

# Create your models here.

class UserProfile(BaseModel):
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username