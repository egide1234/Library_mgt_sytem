from django.contrib import admin
from django.contrib.auth.models import User
from . models import *

class AdminReader(admin.ModelAdmin):
    list_display = ('refrence_id', 'reader_name', 'reader_contact', 'reader_address', 'is_active')
    search_fields = ['refrence_id', 'reader_name']

admin.site.register(Reader, AdminReader)

