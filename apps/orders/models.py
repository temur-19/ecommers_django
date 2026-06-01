from django.db import models

# Create your models here.
from apps.common.models import BaseModel
from django.contrib.auth.models import User

class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"Order of {self.product} (Quantity: {self.quantity})"