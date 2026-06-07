from django.shortcuts import render

from apps.products.models import *


def home(request):
    catigories = Category.objects.all()
    products = Product.objects.all()

    data = {
        "categories": catigories,
        "products": products
    }
    return render(request, "common/home.html", data)
