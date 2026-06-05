from django.shortcuts import render
from .models import Cart


def cart_view(request):
    return render(request, 'savat/savat.html')
