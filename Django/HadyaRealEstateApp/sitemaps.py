from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Property

class PropertySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Property.objects.filter(is_published=True)  # Only public listings

    def location(self, obj):
        return reverse('property_detail', kwargs={'slug': obj.slug})

    def lastmod(self, obj):
        return obj.list_date  # Use your datetime field
