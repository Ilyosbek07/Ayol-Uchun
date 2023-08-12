from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    CourseViewSet, CommentCourseViewSet,
    UnitViewSet, ResourceViewSet,
    VideoViewSet, CommentVideoViewSet,
    VideoWatchProgressViewSet, LikeViewSet,
    ComplainViewSet, UserCourseViewSet, UserCertificateViewSet
)

router = DefaultRouter()

# router.register(r'courses', CourseViewSet)




urlpatterns = [
    path('course/courses/', CourseViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('course/<int:pk>/', CourseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('course/comment-courses/', CommentCourseViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('course/comment-courses/<int:pk>/', CommentCourseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('course/units/', UnitViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('course/units/<int:pk>/', UnitViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('course/resources/', ResourceViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('course/resources/<int:pk>/', ResourceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('course/videos/', VideoViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('course/videos/<int:pk>/', VideoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('course/comment-videos/', CommentVideoViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('course/comment-videos/<int:pk>/', CommentVideoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('course/video-watch-progress/', VideoWatchProgressViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('course/video-watch-progress/<int:pk>/', VideoWatchProgressViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('course/likes/', LikeViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('course/likes/<int:pk>/', LikeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('course/complains/', ComplainViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('course/complains/<int:pk>/', ComplainViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('course/user-courses/', UserCourseViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('course/user-courses/<int:pk>/', UserCourseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('course/user-certificates/', UserCertificateViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('course/user-certificates/<int:pk>/', UserCertificateViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]


