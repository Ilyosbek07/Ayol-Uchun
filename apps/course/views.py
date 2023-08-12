from rest_framework import viewsets
from .models import (
    Course, CommentCourse, Unit, Resource, Video, CommentVideo,
    VideoWatchProgress, Like, Complain, UserCourse, UserCertificate
)
from .serializers import (
    CourseSerializer, CommentCourseSerializer,
    UnitSerializer, ResourceSerializer, VideoSerializer, CommentVideoSerializer,
    VideoWatchProgressSerializer, LikeSerializer, ComplainSerializer, UserCourseSerializer,
    UserCertificateSerializer
)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CommentCourseViewSet(viewsets.ModelViewSet):
    queryset = CommentCourse.objects.all()
    serializer_class = CommentCourseSerializer

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class CommentVideoViewSet(viewsets.ModelViewSet):
    queryset = CommentVideo.objects.all()
    serializer_class = CommentVideoSerializer

class VideoWatchProgressViewSet(viewsets.ModelViewSet):
    queryset = VideoWatchProgress.objects.all()
    serializer_class = VideoWatchProgressSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class ComplainViewSet(viewsets.ModelViewSet):
    queryset = Complain.objects.all()
    serializer_class = ComplainSerializer

class UserCourseViewSet(viewsets.ModelViewSet):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer

class UserCertificateViewSet(viewsets.ModelViewSet):
    queryset = UserCertificate.objects.all()
    serializer_class = UserCertificateSerializer
