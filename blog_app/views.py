from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from .models import Blog
from .serializer import BlogSerializer


# returns list of blogs
@api_view(["GET"])
def blog_list(request):
    blogs = Blog.objects.filter(is_public=True)
    serialized_blogs = BlogSerializer(blogs, many=True)
    return Response(serialized_blogs.data)


# returns detail of a blog
@api_view(["GET"])
def blog_detail(request, pk):
    try:
        blog = Blog.objects.get(is_public=True, id=pk)
        serialized_blog = BlogSerializer(blog)
        return Response(serialized_blog.data)
    except ObjectDoesNotExist:
        return Response(
            {
                "error": "blog with provided id doesn't exist",
            },
            status=404,
        )
