from django.db import models
from apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    