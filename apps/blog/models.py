from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

from apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Author(BaseModel):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


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
    author = models.ForeignKey(
        "blog.Author",
        on_delete=models.CASCADE,
        related_name="blog",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        "blog.Category",
        on_delete=models.CASCADE,
        related_name="blog",
        null=True,
        blank=True,
    )
    content = RichTextUploadingField(null=True)
    cover = models.ImageField(upload_to="blog/images/", null=True, blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title


class BlogView(BaseModel):
    blog = models.ForeignKey("blog.Blog", on_delete=models.CASCADE, related_name="view")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_view")

    def __str__(self):
        return f"View of '{self.blog.title}' from {self.user}"
