from rest_framework import viewsets
from rest_framework.response import Response

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
from .serializers import (
    CourseSerializer,
    CommentCourseSerializer,
    UnitSerializer,
    ResourceSerializer,
    VideoSerializer,
    CommentVideoSerializer,
    VideoWatchProgressSerializer,
    LikeSerializer,
    ComplainSerializer,
    UserCourseSerializer,
    UserCertificateSerializer,
    AuthorSerializer,
    CategorySerializer,
)
from .filters import CourseFilter


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filterset_class = CourseFilter

    def get_serializer_context(self, **kwargs):
        context = super(CourseViewSet, self).get_serializer_context()
        user_id = self.request.user.id
        context.update({'user_id': user_id})
        return context


class CommentCourseViewSet(viewsets.ModelViewSet):
    queryset = CommentCourse.objects.all()
    serializer_class = CommentCourseSerializer

    def list(self, request, pk=None):
        queryset = self.get_queryset().filter(course=pk).order_by('created_at')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)



class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    def list(self, request, pk=None):
        queryset = self.get_queryset().filter(course=pk).order_by('order')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)



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
