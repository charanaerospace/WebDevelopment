#The `urlpatterns` list defines the URL patterns for the listings app. It includes three paths:
#- The root path (`/`) maps to the `index` view, which likely displays a list of all listings.
#- The path `/<int:listing_id>` maps to the `listing` view, which likely displays details of a specific listing.
#- The path `/search` maps to the `search` view, which likely handles search functionality for the listings.

from django.contrib import admin
from django.urls import path,include
from .import views
#listings/23
urlpatterns = [
    path('', views.index,name="listings"),
    path('<int:listing_id>', views.listing,name="listing"),
    path('search', views.search, name="search"),

]