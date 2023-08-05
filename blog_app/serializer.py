from rest_framework import serializers
from blog_app.models import Blog, Category


# ----------------Model serializer----------------
class BlogSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        # Get only specific fields in response:
        fields = [
            "id",
            "blog_title",
            "author",
            "blog_description",
            "is_public",
            "category",
        ]
        # Get all fields in response:
        # fields = "__all__"
        # Exclude certain fields:
        # exclude = ["slug"]

    # overriding category field with the name of category instead of id using serializer method fields
    def get_category(self, object):
        return object.category.category_name if object.category else None

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
    # Get Custom method fields in serializers in responses
    # New key value  in our response i.e. len of blog's title
    # you also have to set the fields name in fields above in class Meta if not used fields as __all__
    len_blog_title = serializers.SerializerMethodField()

    def get_len_blog_title(self, object):
        return len(object.blog_title)
    """


class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField()
    # Display  all blogs and its detials related to a category
    category = BlogSerializer(many=True, read_only=True)
    '''
    RELATED FIELDS:
    # ?1.StringRelatedField: Display only blog title related to the category
    category = serializers.StringRelatedField(many=True)
    # ?2. PrimaryKeyRelatedField: Display only primarykey field of related bolgs
    category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    """ 3. HyperLinkRelatedField: Display hyperLinked related field which directly provides link
        to the related blog We have to pass view_name i.e.name given in urls.py, to its option
        and also pass context={'request':request} to our category serializers options in view
    """
    category = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name="blog_detail"
    # )
    # ?4. SlugRelatedField: Display slug field of related blogs in response api
    category = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="slug"
    )
    '''

    class Meta:
        model = Category
        exclude = ["id"]


"""
HYPERLINKED MODEL SERIALIZER:
It serialized model and returns the link/url inplace of id or primarly key in its reponse which
links to that category or models response detail. You also have to make your url name if like 
category_detail to category-detail

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    category_name = serializers.CharField()
    category = BlogSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"
"""


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
