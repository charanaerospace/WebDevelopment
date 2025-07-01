#+ The `list_display_links` attribute in the `ContactAdmin` class specifies the fields in the `Contact`
#  model that should be displayed as links in the Django admin interface.
#  This allows users to navigate to the detail view of a specific contact by clicking on the ID or name fields in the admin list view.
#  The `search_fields` attribute specifies the fields in the `Contact` model that should be searched when performing a search in the admin interface.
#  This allows users to quickly find specific contacts by searching for their name, email, or listing ID.
#  The `list_per_page` attribute specifies the number of contacts to display per page in the admin list view.
#  This allows users to navigate through the list of contacts in smaller chunks, rather than displaying all contacts at once.
#  Overall, these attributes in the `ContactAdmin` class help to improve the usability and functionality of the Django admin interface for the `Contact` model.

from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'listing', 'email', 'contact_date')
  list_display_links = ('id', 'name','email')
  search_fields = ('name', 'email', 'listing')
  list_per_page = 25

admin.site.register(Contact, ContactAdmin)


