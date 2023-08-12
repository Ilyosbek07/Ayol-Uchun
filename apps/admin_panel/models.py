from django.db import models
from apps.accounts.models import Profile
from apps.blog.models import Blog
from apps.common.models import BaseModel


class SocialMedia(BaseModel):
    name = models.CharField(max_length=255)
    link = models.URLField()
    photo = models.ImageField(upload_to="social_media_photos/")

    def __str__(self):
        return self.name


class Contact(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=125)
    text = models.TextField()

    def __str__(self):
        return self.name


class Interview(BaseModel):
    profile = models.ForeignKey(
        Profile, related_name="interviews", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to="interview_videos/")
    url = models.URLField()
    thumbnail = models.ImageField(upload_to="interview_thumbnails/")
    description = models.TextField()

    def __str__(self):
        return self.title


class Notification(BaseModel):
    STATUS_CHOICES = [
        ("moderation", "Moderation"),
        ("published", "Published"),
        ("archived", "Archived"),
    ]

    name = models.CharField(max_length=255)
    blog_id = models.ForeignKey(
        Blog, related_name="notifications", on_delete=models.CASCADE
    )
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name
