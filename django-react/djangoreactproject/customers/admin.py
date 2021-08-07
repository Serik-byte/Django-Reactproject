from django.contrib import admin
from .models import *
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone')
    list_display_links = ('id', 'first_name', 'last_name', 'email', 'phone')
    search_fields = ('id', 'first_name', 'last_name', 'email', 'phone')


admin.site.register(Customer, CustomerAdmin)