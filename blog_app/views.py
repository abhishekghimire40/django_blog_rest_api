from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from .models import Blog, Category
from .serializer import BlogSerializer, CategorySerializer


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serialized_data = CategorySerializer(
            categories, many=True, context={"request": request}
        )
        return Response(serialized_data.data, 200)


class CategoryDetailView(APIView):
    def get(self, request, pk):
        try:
            single_category = Category.objects.get(id=pk)
            serialized_category = CategorySerializer(
                single_category, context={"request": request}
            )
            return Response(serialized_category.data, 200)
        except:
            return self.errorResponse()

    def errorResponse(self):
        return Response(
            {
                "error": "Category with provided id doesn't exist",
            },
            status=404,
        )


class BlogListView(APIView):
    def get(self, request):
        blogs = Blog.objects.filter(is_public=True)
        serialized_blogs = BlogSerializer(blogs, many=True)
        return Response(serialized_blogs.data)

    def post(self, request):
        serialized_data = BlogSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=201)
        return Response(serialized_data.errors, status=400)


class BlogDetailView(APIView):
    def get(self, request, pk):
        try:
            blog = Blog.objects.get(is_public=True, id=pk)
            serialized_data = BlogSerializer(blog)
            return Response(serialized_data.data, status=200)
        except ObjectDoesNotExist:
            return self.errorResponse()

    def put(self, request, pk):
        try:
            blog = Blog.objects.get(is_public=True, id=pk)
            serialized_data = BlogSerializer(blog, data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(serialized_data.data, status=201)
            return Response(serialized_data.errors, status=400)
        except ObjectDoesNotExist:
            return self.errorResponse()

    def delete(self, request, pk):
        try:
            blog = Blog.objects.get(id=pk)
            blog.delete()
            return Response(status=204)
        except ObjectDoesNotExist:
            return self.errorResponse()

    def errorResponse(self):
        return Response(
            {
                "error": "Blog with provided id doesn't exist",
            },
            status=404,
        )


"""
---------------------------Function based View--------------------------------
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
                return Response(serialized_blog.data, status=201)
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
"""
