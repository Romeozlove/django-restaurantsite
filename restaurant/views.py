from django.shortcuts import render
from .models import Menu,CATEGORY_CHOICES
# Create your views here.

def index(request):
    return render(request, 'restaurant/index.html')

def menu(request):
    categories = CATEGORY_CHOICES
    menu_items = len(CATEGORY_CHOICES)
    return render(request,'restaurant/menu.html',{'categories':categories,'menu_items':range(menu_items)})