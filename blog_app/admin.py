from django.contrib import admin

# Register your models here.
from .models import Blog, BlogComment

admin.site.register(Blog)
admin.site.register(BlogComment)
