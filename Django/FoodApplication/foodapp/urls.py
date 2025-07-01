from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #path(" ", views.hello,name="hello"),
    path("", views.home, name="home")
]
