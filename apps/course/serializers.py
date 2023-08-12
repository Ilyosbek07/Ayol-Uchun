from rest_framework import serializers
from .models import (
    Course, CommentCourse, Unit, Resource, Video, CommentVideo,
    VideoWatchProgress, Like, Complain, UserCourse, UserCertificate
)

class UserCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCertificate
        fields = '__all__'

class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = '__all__'

class UserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = '__all__'

class CommentVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentVideo
        fields = '__all__'

class VideoWatchProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoWatchProgress
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    comment_video = CommentVideoSerializer(many=True, read_only=True)
    video_watch_progress = VideoWatchProgressSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Unit
        fields = '__all__'

class CommentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentCourse
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    comment_course = CommentCourseSerializer(many=True, read_only=True)
    units = UnitSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
