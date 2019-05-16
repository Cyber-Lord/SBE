from django.shortcuts import render
from .models import *
# Create your views here.

def bank(request):
    banks = Bank.objects.all()
    return render(request, 'iplus/home.html', {"yyy": banks})