from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/blogs/", include("blog_app.urls")),
    path("api-auth/", include("rest_framework.urls")),
]
