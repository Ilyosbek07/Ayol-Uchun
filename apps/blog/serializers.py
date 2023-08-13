from rest_framework import serializers

from apps.blog.models import Blog, Category


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class ListBlogWithCategorySerializer(serializers.ModelSerializer):
    blog_view = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = (
            "id",
            "title",
            "author",
            "category",
            "cover",
            "blog_view",
            "created_at",
            "updated_at",
        )

    def get_blog_view(self, obj):
        return obj.view.all().count()


class BlogListSerializer(serializers.ModelSerializer):
    blog_view = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = (
            "id",
            "title",
            "author",
            "category",
            "cover",
            "blog_view",
            "created_at",
            "updated_at",
        )

    def get_blog_view(self, obj):
        return obj.view.all().count()


class BlogDetailView(serializers.ModelSerializer):
    blog_view = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = (
            "id",
            "title",
            "author",
            "category",
            "content",
            "cover",
            "status",
            "blog_view",
            "created_at",
        )

    def get_blog_view(self, obj):
        return obj.view.all().count()
