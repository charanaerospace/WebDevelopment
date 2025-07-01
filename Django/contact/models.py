"""
Represents a contact made by a user for a specific listing.

The `Contact` model stores information about a user's contact with a real estate listing,
including the listing details, the user's name, email, phone, and message, as well as the date of the contact.
It also stores the ID of the user who made the contact and the email of the realtor associated with the listing,
if available.
"""

from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.utils.timezone import now

class Contact(models.Model):
  # user = models.ForeignKey(User, on_delete=models.CASCADE)
  listing = models.CharField(max_length=200)
  listing_id = models.IntegerField()
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  user_id = models.IntegerField(blank=True,null=True)
  realtor_email = models.EmailField(max_length=100, blank=True, null=True)
  def __str__(self):
    return self.name if self.name else "Unnamed Contact"
    #return f"Contact: Listing {self.listing} (ID: {self.listing_id}), User ID: {self.user_id}, Date: {self.contact_date}"

