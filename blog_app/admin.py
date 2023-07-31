from django.contrib import admin

# Register your models here.
from .models import Blog, BlogComment, Category


# styling and functionality for admin panel
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "blog_title", "author", "category", "post_date", "is_public")
    list_display_links = ("id", "blog_title")
    search_fields = ("name", "author", "category")
    list_editable = ("is_public", "category")
    list_per_page = 20


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment)
