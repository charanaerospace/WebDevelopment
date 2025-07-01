#The `urlpatterns` list defines the URL patterns for the Django application.
# It maps URL paths to the corresponding views, which handle the logic for rendering the pages.
# This includes the home page (`/`), the about page (`/about/`), the privacy policy page (`/privacy/`),
# and the contact us page (`/contactus/`).


from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('about/', views.about,name="about"),
    path('privacy/', views.privacy,name="privacy"),
    path('contactus/', views.contactus,name="contactus"),
    path('property/<slug:slug>/', views.property_detail,name="property_detail")

]