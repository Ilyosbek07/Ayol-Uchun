from django.db.models import Count
from rest_framework import serializers
from .utils import get_video_length
from .models import (
    Course,
    CommentCourse,
    Unit,
    Resource,
    Video,
    CommentVideo,
    VideoWatchProgress,
    UserCourse,
    UserCertificate,
    Author,
    Category,
)


class UserCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCertificate
        fields = "__all__"


class UserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = "__all__"


class ReplyCommentVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentVideo
        fields = "__all__"


class CommentVideoSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CommentVideo
        fields = (
            "id",
            "profile",
            "video",
            "main_comment",
            "parent_comment",
            "text",
            "replies",
        )

    def get_replies(self, obj):
        data = CommentVideo.objects.filter(main_comment=obj.id)
        serializer = ReplyCommentVideoSerializer(data, many=True)
        return serializer.data


class VideoWatchProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoWatchProgress
        fields = "__all__"


class VideoSerializer(serializers.ModelSerializer):
    video_watch_progress = VideoWatchProgressSerializer(many=True, read_only=True)
    is_finished = serializers.SerializerMethodField(read_only=True)
    video_length = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Video
        fields = (
            "id",
            "title",
            "is_finished",
            "unit",
            "video",
            "video_url",
            "video_length",
            "resource",
            "description",
            "order",
            "video_watch_progress",
        )

    def get_is_finished(self, obj):
        user_id = self.context.get("user_id")
        if VideoWatchProgress.objects.filter(profile=user_id, video=obj.id).exists():
            return True
        return False

    def get_video_length(self, obj):
        path = "/Users/sarvarrahmonov/Desktop/Projects/Ayol-Uchun/media/%s" % obj.video
        lenght_of_video = get_video_length(path)
        return lenght_of_video


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = "__all__"


class CommentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentCourse
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)
    category_name = serializers.CharField(source="category.name", read_only=True)
    author_count = serializers.SerializerMethodField()
    discount_price = serializers.SerializerMethodField(read_only=True, default=0)
    is_bought = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = (
            "id",
            "author",
            "author_count",
            "category_name",
            "title",
            "status",
            "is_bought",
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
            "average_rate",
        )

    def get_author_count(self, obj):
        return obj.author.count()

    def get_discount_price(self, instance):
        if instance.discount > 0:
            price = instance.price
            discount_price = (instance.discount / 100) * price
            return int(discount_price)

    def get_is_bought(self, instance):
        user_id = self.context.get("user_id")
        if UserCourse.objects.filter(profile=user_id, course=instance.id):
            return True
        return False


class UnitSerializer(serializers.ModelSerializer):
    course = serializers.CharField(source="course.title")
    videos_of_unit = VideoSerializer(many=True, read_only=True)
    is_bought = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Unit
        fields = (
            "id",
            "course",
            "title",
            "is_bought",
            "status",
            "order",
            "videos_of_unit",
        )

    def get_is_bought(self, instance):
        user_id = self.context.get("user_id")
        course_id = self.context.get("course_id")
        if UserCourse.objects.filter(profile=user_id, course=course_id):
            return True
        return False

    def get_status(self, instance):
        user_id = self.context.get("user_id")
        course_id = self.context.get("course_id")
        watched_video_count = VideoWatchProgress.objects.filter(
            video__unit__course_id=course_id,
            video__unit_id=instance.id,
            profile=user_id,
        ).aggregate(video_count=Count("video"))["video_count"]
        unit_video_count = Video.objects.filter(unit_id=instance.id).count()
        if watched_video_count == 0:
            return "Ko'rilmagan"
        elif watched_video_count > 0 and watched_video_count < unit_video_count:
            return "Jarayonda"
        elif watched_video_count == unit_video_count:
            return "Ko'rilgan"


class CategorySerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("id", "name", "category")
