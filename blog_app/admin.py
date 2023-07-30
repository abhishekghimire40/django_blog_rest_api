from django.contrib import admin

# Register your models here.
from .models import Blog, BlogComment


# styling and functionality for admin panel
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "author", "post_date", "is_public")
    list_display_links = ("id", "name")
    search_fields = ("name", "author")
    list_editable = ("is_public",)
    list_per_page = 20


admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment)
