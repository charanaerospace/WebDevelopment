from django.shortcuts import render # type: ignore
# Create your views here.
from django.http import HttpResponse

def hello(request):
    return  HttpResponse("Hello World")

    