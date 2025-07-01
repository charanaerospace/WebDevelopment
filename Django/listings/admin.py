#The `ListingAdmin` class is a Django admin model that provides a customized interface for managing
#- `Listing` objects in the Django admin panel. It defines various display and filtering options for the admin interface,
#   including:
#- `list_display`: Specifies the fields to be displayed in the admin list view.
#- `list_display_links`: Specifies the fields that should be used as links to the object detail page.
#- `list_filter`: Specifies the fields that should be used for filtering the admin list view.
#- `list_editable`: Specifies the fields that can be edited directly in the admin list view.
#- `search_fields`: Specifies the fields that should be used for searching the admin list view.
#- `list_per_page`: Specifies the number of objects to be displayed per page in the admin list view.


from django.contrib import admin
from  .models import Listing
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','list_date','realtor')
    list_display_links = ('id','title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title','description','address','city','state','zip_code','price')
    list_per_page=25
admin.site.register(Listing,ListingAdmin)