from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    CourseViewSet,
    CommentCourseViewSet,
    UnitViewSet,
    VideoViewSet,
    CommentVideoViewSet,
    UserCourseViewSet,
    UserCertificateViewSet,
    CategoryViewSet,
)

router = DefaultRouter()



urlpatterns = [
    path("courses/", CourseViewSet.as_view({"get": "list", "post": "create"})),
    path("categories/", CategoryViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "course_detail/<int:pk>/",
        CourseViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
    path(
        "comment-courses/<int:pk>/",
        CommentCourseViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "<int:pk>/comments",
        CommentCourseViewSet.as_view(
            {"get": "list", "put": "update", "delete": "destroy"}
        ),
    ),
    path("<int:pk>/units/", UnitViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "video/<int:pk>/",
        VideoViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
    path(
        "video-comments/<int:pk>/",
        CommentVideoViewSet.as_view(
            {"get": "retrieve", "put": "update", "post": "create", "delete": "destroy"}
        ),
    ),
    path(
        "user-courses/<int:pk>/",
        UserCourseViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
    path(
        "user-certificates/<int:pk>/",
        UserCertificateViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
]


