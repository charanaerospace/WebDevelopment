
from django.urls import path

from . import views

urlpatterns = [
  path('contact/', views.contact, name='contact')
# Handles the contact form submission for a property listing.
# When a user submits the contact form for a property listing, this view processes the form data, checks if the user has already contacted about the listing, saves the contact information, and sends an email notification to the realtor.
# Args:
#     request (django.http.HttpRequest): The HTTP request object containing the form data.
 
# Returns:
#     django.http.HttpResponse: A redirect response to the property listing page.

]

