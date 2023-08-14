from rest_framework import viewsets, permissions
from rest_framework.response import Response
from apps.accounts.models import Profile
from .models import (
    Course,
    CommentCourse,
    Unit,
    Video,
    CommentVideo,
    VideoWatchProgress,
    UserCourse,
    UserCertificate,
    Category,
)
from .serializers import (
    CourseSerializer,
    CommentCourseSerializer,
    UnitSerializer,
    VideoSerializer,
    CommentVideoSerializer,
    UserCourseSerializer,
    UserCertificateSerializer,
    CategorySerializer,
)
from .filters import CourseFilter


class AdminAccessPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ["post", "put", "update", "delete", "destroy"]:
            return request.user.is_authenticated and request.user.is_staff
        return True


# ----------------------------------------------------------------


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filterset_class = CourseFilter

    def get_serializer_context(self, **kwargs):
        context = super(CourseViewSet, self).get_serializer_context()
        user_id = self.request.user.id
        context.update({"user_id": user_id})
        return context


class CommentCourseViewSet(viewsets.ModelViewSet):
    queryset = CommentCourse.objects.all()
    serializer_class = CommentCourseSerializer

    def list(self, request, pk=None):
        queryset = self.get_queryset().filter(course=pk).order_by("created_at")
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [AdminAccessPermissions]

    def list(self, request, pk=None):
        queryset = self.get_queryset().filter(course=pk).order_by("order")
        serializer = self.serializer_class(
            queryset, many=True, context={"user_id": request.user.id, "course_id": pk}
        )
        return Response(serializer.data)


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [AdminAccessPermissions]

    def retrieve(self, request, pk=None):
        instance = Video.objects.get(pk=pk)
        profile = Profile.objects.get(user=request.user.id)
        obj = VideoWatchProgress.objects.get_or_create(
            profile=profile, video=instance, last_viewed_seconds=1, is_completed=True
        )
        serializer = self.serializer_class(
            instance=instance, context={"user_id": request.user.id}
        )
        return Response(serializer.data)


class CommentVideoViewSet(viewsets.ModelViewSet):
    queryset = CommentVideo.objects.all()
    serializer_class = CommentVideoSerializer

    def retrieve(self, request, pk=None):
        instance = CommentVideo.objects.filter(
            video=pk, main_comment__isnull=True
        ).all()
        serializer = self.serializer_class(instance=instance, many=True)
        return Response(serializer.data)



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class UserCourseViewSet(viewsets.ModelViewSet):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer


class UserCertificateViewSet(viewsets.ModelViewSet):
    queryset = UserCertificate.objects.all()
    serializer_class = UserCertificateSerializer
