from django.urls import path
from . import views


urlpatterns = [
    # Blog urls
    path("blog_list/", views.BlogListView.as_view(), name="blogs_list"),
    path("blog_detail/<int:pk>/", views.BlogDetailView.as_view(), name="blog_detail"),
    # Category urls
    path("category_list/", views.CategoryListView.as_view(), name="category_list"),
    path(
        "category_detail/<int:pk>/",
        views.CategoryDetailView.as_view(),
        name="category_detail",
    ),
]


# function based view urls
# urlpatterns = [
#     path("blog_list/", views.blog_list, name="blog_list"),
#     path("blog_detail/<int:pk>/", views.blog_detail, name="blog_detail"),
# ]
