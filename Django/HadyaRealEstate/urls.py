"""
URL configuration for HadyaRealEstate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from dill import settings
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from HadyaRealEstateApp.sitemaps import PropertySitemap
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap

sitemaps= {'properties': PropertySitemap}
urlpatterns = [
    path("admin/", admin.site.urls),
    path('listings/',include('listings.urls')),
    path('accounts/',include('accounts.urls')),
    path('contact/',include('contact.urls')),
    path("", include("HadyaRealEstateApp.urls")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
