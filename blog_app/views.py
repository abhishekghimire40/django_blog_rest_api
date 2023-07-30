from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Blog


# returns list of blogs
def blog_list(request):
    blogs = Blog.objects.all()
    # data = {"blogs": list(blogs.values())}
    data = {"blogs": list(blogs.values())}
    return JsonResponse(data)


# returns detail of a blog
def blog_detail(request, pk):
    try:
        blog = Blog.objects.get(id=pk)
        data = {
            "name": blog.name,
            "description": blog.description,
            "slug": blog.slug,
        }
        return JsonResponse(data)
    except ObjectDoesNotExist:
        return JsonResponse(
            {
                "error": "blog with provided id doesn't exist",
            },
            status=404,
        )
