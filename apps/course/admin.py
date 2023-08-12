from django.contrib import admin
from .models import (
    Author,
    Category,
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
)
from apps.accounts.models import Profile, Country, Region, Position

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(CommentCourse)
admin.site.register(Unit)
admin.site.register(Resource)
admin.site.register(Video)
admin.site.register(CommentVideo)
admin.site.register(VideoWatchProgress)
admin.site.register(Like)
admin.site.register(Complain)
admin.site.register(UserCourse)
admin.site.register(UserCertificate)
admin.site.register(Profile)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(Position)
