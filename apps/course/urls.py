from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    CourseViewSet,
    CommentCourseViewSet,
    UnitViewSet,
    ResourceViewSet,
    VideoViewSet,
    CommentVideoViewSet,
    VideoWatchProgressViewSet,
    LikeViewSet,
    ComplainViewSet,
    UserCourseViewSet,
    UserCertificateViewSet,
    CategoryViewSet,
)

router = DefaultRouter()

# router.register(r'courses', CourseViewSet)


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
        "comment-courses/",
        CommentCourseViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "comment-courses/<int:pk>/",
        CommentCourseViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
    path("units/", UnitViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "units/<int:pk>/",
        UnitViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
    path("resources/", ResourceViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "resources/<int:pk>/",
        ResourceViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
    path("videos/", VideoViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "videos/<int:pk>/",
        VideoViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
    path(
        "comment-videos/",
        CommentVideoViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "comment-videos/<int:pk>/",
        CommentVideoViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
    path(
        "video-watch-progress/",
        VideoWatchProgressViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "video-watch-progress/<int:pk>/",
        VideoWatchProgressViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
    path("likes/", LikeViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "likes/<int:pk>/",
        LikeViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
    path("complains/", ComplainViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "complains/<int:pk>/",
        ComplainViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
    path("user-courses/", UserCourseViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "user-courses/<int:pk>/",
        UserCourseViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
    path(
        "user-certificates/",
        UserCertificateViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "user-certificates/<int:pk>/",
        UserCertificateViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
]
