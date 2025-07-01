"""
Handles the contact form submission for a property listing.

When a user submits the contact form for a property listing, this view processes the form data, checks if the user has already contacted about the listing, saves the contact information, and sends an email notification to the realtor.

Args:
    request (django.http.HttpRequest): The HTTP request object containing the form data.

Returns:
    django.http.HttpResponse: A redirect response to the property listing page.
"""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
  if request.method == 'POST':
    listing_id = request.POST['listing_id']
    listing  = request.POST['listing']
    name  = request.POST['name']
    email  = request.POST['email']
    phone  = request.POST['phone']
    message  = request.POST['message']
    user_id   =request.POST['user_id']
    realtor_email   =request.POST['realtor_email']

    #Check user made an enquirty already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have already made an enquiry for this listing')
        return redirect('/listings/' + listing_id)

    contact =Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id,realtor_email=realtor_email)

    contact.save()

    #Send Email
    # send_mail('Property Listing Enquiry',
    #           'There has been an enquiry for ' + listing + '. Sign into the admin panel for more info',
    #           '',
    #           [realtor_email, '],
    #           fail_silently=False
    #           )



    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('/listings/'+listing_id)




