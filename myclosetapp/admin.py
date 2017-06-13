from django.contrib import admin

# Register your models here.
from .models import Profile, Category, Item

# Register your models here.
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Item)

