from django.contrib import admin
from .models import *
# Register your models here.

class demoadmin(admin.ModelAdmin):
    list_display = ['name','is_active']
admin.site.register(Demo,demoadmin)