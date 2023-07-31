from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from datetime import date
from .models import Blog
from .serializer import BlogSerializer


# returns list of blogs
@api_view(["GET", "POST"])
def blog_list(request):
    if request.method == "POST":
        serialized_data = BlogSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=201)
        else:
            return Response(serialized_data.errors)
    blogs = Blog.objects.filter(is_public=True)
    serialized_blogs = BlogSerializer(blogs, many=True)
    return Response(serialized_blogs.data)


# returns detail of a blog
@api_view(["GET", "PUT", "DELETE"])
def blog_detail(request, pk):
    try:
        blog = Blog.objects.get(is_public=True, id=pk)

        # for put requests
        if request.method == "PUT":
            serialized_blog = BlogSerializer(blog, data=request.data)
            if serialized_blog.is_valid():
                serialized_blog.save()
                return Response(serialized_blog.data)
            else:
                return Response(serialized_blog.errors, status=400)

        # for delete requests
        if request.method == "DELETE":
            blog.delete()
            return Response(status=204)

        serialized_blog = BlogSerializer(blog)
        return Response(serialized_blog.data)
    except ObjectDoesNotExist:
        return Response(
            {
                "error": "blog with provided id doesn't exist",
            },
            status=404,
        )
