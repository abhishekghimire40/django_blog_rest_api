from rest_framework import serializers
from blog_app.models import Blog


# ----------------Model serializer----------------
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        # Get only specific fields in response:
        fields = ["id", "blog_title", "author", "blog_description", "is_public"]
        # Get all fields in response:
        # fields = "__all__"
        # Exclude certain fields:
        # exclude = ["slug"]

    # field-level validation
    def validate_blog_title(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("Blog title is too short!")
        else:
            return value

    # Object-level validation
    def validate(self, data):
        if len(data["blog_description"]) < 4:
            raise serializers.ValidationError("Description is too short!")
        elif data["blog_title"] == data["blog_description"]:
            raise serializers.ValidationError(
                "title and description of blog cannot be same"
            )
        else:
            return data


"""
# --------normal serializer for  blog model ;manual-----------------
class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    author = serializers.CharField()
    description = serializers.CharField()
    post_date = serializers.DateTimeField()
    is_public = serializers.BooleanField()
    slug = serializers.CharField()

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.author = validated_data.get("author", instance.author)
        instance.description = validated_data.get("description", instance.description)
        instance.is_public = validated_data.get("is_public", instance.is_public)
        instance.post_date = validated_data.get("post_date", instance.post_date)
        instance.slug = validated_data.get("slug", instance.slug)
        instance.save()
        return instance
"""
