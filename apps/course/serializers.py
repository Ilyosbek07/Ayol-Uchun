from rest_framework import serializers
from .models import (
    Course,
    CommentCourse,
    Unit,
    Resource,
    Video,
    CommentVideo,
    VideoWatchProgress,
    Like,
    Complain,
    UserCourse,
    UserCertificate,
    Author,
    Category,
)


class UserCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCertificate
        fields = "__all__"


class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = "__all__"


class UserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = "__all__"


class CommentVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentVideo
        fields = "__all__"


class VideoWatchProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoWatchProgress
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class VideoSerializer(serializers.ModelSerializer):
    comment_video = CommentVideoSerializer(many=True, read_only=True)
    video_watch_progress = VideoWatchProgressSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = "__all__"


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = "__all__"


class UnitSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Unit
        fields = "__all__"


class CommentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentCourse
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    author_names = serializers.StringRelatedField(many=True, source="author")
    category_name = serializers.CharField(source="category.name", read_only=True)
    author_count = serializers.SerializerMethodField()
    discount_price = serializers.SerializerMethodField(read_only=True, default=0)

    class Meta:
        model = Course
        fields = (
            "id",
            "author_names",
            "author_count",
            "category_name",
            "title",
            "status",
            "is_recommended",
            "is_bestseller",
            "image",
            "price",
            "discount_price",
            "discount",
            "is_active",
            "certificate",
            "currency",
            "description",
            "avarage_rate",

        )

    def get_author_count(self, obj):
        return obj.author.count()


    def get_discount_price(self, instance):
        if instance.discount > 0:
            price = instance.price
            discount_price = (instance.discount / 100) * price
            return int(discount_price)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("name", "category")
