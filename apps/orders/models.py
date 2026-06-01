from django.db import models

# Create your models here.
from apps.common.models import BaseModel

class Order(BaseModel):
    product = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Order of {self.product} (Quantity: {self.quantity})"