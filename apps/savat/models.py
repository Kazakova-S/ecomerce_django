from django.db import models
from django.contrib.auth.models import User
from apps.products.models import Product
from apps.common.models import BaseModel


# Savatcha - foydalanuvchi mahsulotlarni shu yerga soladi
class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)       # Qaysi foydalanuvchi
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # Qaysi mahsulot
    quantity = models.PositiveIntegerField(default=1)              # Nechta

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
    