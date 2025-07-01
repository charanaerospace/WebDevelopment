#The RealtorAdmin class is a Django admin model that provides a customized interface for managing Realtor objects in the a
#Admin panel.
#It defines various display and filtering options, such as the list of fields to display, the fields to use for searching,
#and the fields to use for filtering. This allows the admin user to easily view, search,
#and filter the list of realtors in the admin panel.


from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_mvp', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('is_mvp', 'hire_date')
    list_per_page = 25
    readonly_fields = ('hire_date',)

admin.site.register(Realtor, RealtorAdmin)
