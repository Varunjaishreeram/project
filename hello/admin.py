from django.contrib import admin

# Register your models here.
# hello/admin.py

from .models import Vendor

admin.site.register(Vendor)
