#The `index` function is the main view function for the home page of the Hadya Real Estate application.
# It retrieves the three most recently published listings and passes them, along with some choice data, to the `index.html`
# template for rendering.
#The `about` function is the view function for the about page.
# It retrieves all realtors, ordered by their hire date, and the "MVP" realtors (those with `is_mvp=True`),
# and passes them to the `about.html` template for rendering.
#The `privacy` function is the view function for the privacy page.
# It simply renders the `privacy.html` template.
#The `contactus` function is the view function for the contact page.
# It retrieves the "MVP" realtors (those with `is_mvp=True`) and passes them to the `contact.html` template for rendering.



from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import  price_choices, bedroom_choices, state_choices

# Create your views here.

def index(request):
    listing=Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings':listing,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices
    }
    return render(request,'HadyaRealEstateApp/index.html',context)
    #return HttpResponse('<h1>Hello World</h1>')

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    #get
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context={
        'realtors':realtors,
        'mvp_realtors':mvp_realtors
    }

    return render(request,'HadyaRealEstateApp/about.html',context)

def privacy(request):
    return render(request,'HadyaRealEstateApp/privacy.html')

def contactus(request):
    mvp_realtors = Realtor.objects.filter(is_mvp=True)  # Adjust the filter based on your model
    context = {
        'mvp_realtors': mvp_realtors,
    }
    return render(request, 'HadyaRealEstateApp/contact.html', context)

def property_detail(request, slug):
    property = get_object_or_404(Listing, slug=slug)

    context = {
        'property': property,
        'meta_title': f"{property.title} | Hadya Real Estate",
        'meta_description': property.description[:160],
    }
    return render(request, 'property_detail.html', context)
