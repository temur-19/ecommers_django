from django.db import models

# Create your models here.
from apps.common.models import BaseModel
from django.contrib.auth.models import User
from apps.products.models import Product
from project import settings

class Order(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.phone_number}"  
      
class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.product}"