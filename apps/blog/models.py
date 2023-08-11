from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator
from django.db import models

from apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class File(BaseModel):
    VIDEO = "video"
    IMAGE = "image"
    TYPE_CHOICES = [
        (VIDEO, "Video"),
        (IMAGE, "Image"),
    ]

    file = models.FileField(
        upload_to="blog/files/",
        validators=[FileExtensionValidator(allowed_extensions=["mp4", "avi", "mov", "jpg", "jpeg", "heic", "png"])],
        null=True,
        blank=True,
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return self.file.name


class Blog(BaseModel):
    MODERATION = "moderation"
    PUBLISHED = "published"
    ARCHIVED = "archived"
    STATUS_CHOICES = [
        (MODERATION, "Moderation"),
        (PUBLISHED, "Published"),
        (ARCHIVED, "Archived"),
    ]

    title = models.CharField(max_length=64)
    # profile = models.ForeignKey()
    description = RichTextField()
    category = models.ForeignKey("blog.Category", on_delete=models.CASCADE, related_name="blog", null=True)
    content = models.ForeignKey(
        "blog.File",
        on_delete=models.CASCADE,
        related_name="content",
        null=True,
        blank=True,
    )
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title


class View(BaseModel):
    blog = models.ForeignKey("blog.Blog", on_delete=models.CASCADE, related_name="view")
    device_id = models.CharField(max_length=100)

    def __str__(self):
        return f"View of '{self.blog.title}' from device ID {self.device_id}"
