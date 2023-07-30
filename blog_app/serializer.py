from rest_framework import serializers


# serializer for  blog model
class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    author = serializers.CharField()
    description = serializers.CharField()
    post_date = serializers.DateTimeField()
    is_public = serializers.BooleanField()
    slug = serializers.CharField()
