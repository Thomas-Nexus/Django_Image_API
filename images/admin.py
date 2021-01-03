from django.contrib import admin
from .models import *
from . import models



admin.site.register(Images)

class Author(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': 'title'}

admin.site.register(Category)