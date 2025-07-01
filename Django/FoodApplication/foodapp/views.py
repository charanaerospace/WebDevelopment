from django.shortcuts import render
from django.http import HttpResponse
from .models import Food_items
# Create your views here.
def hello(request):
    return HttpResponse("Hello World")

def home(request):
    item_list=Food_items.objects.all()
    return  render (item_list)