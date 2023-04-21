from django.contrib import admin
from .models import List, Restaurant, Comment

# Register your models here.
admin.site.register(List)
admin.site.register(Restaurant)
admin.site.register(Comment)