from django.contrib import admin
from .models import *


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


