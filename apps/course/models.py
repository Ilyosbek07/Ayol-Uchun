from django.db import models
from ckeditor.fields import RichTextField

from apps.accounts.models import Profile
from apps.common.models import BaseModel


class Unit(models.Model):
    title = models.CharField(max_length=600)

    def __str__(self):
        return self.title


class Course(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    )
    CURRENCY_CHOICES = (
        ('usd', 'USD'),
        ('eur', 'EUR'),
        ('uzs', 'UZS'),
    )
    profiles = models.ManyToManyField(Profile)
    title = models.CharField(max_length=600)
    units = models.ManyToManyField(Unit)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    image = models.ImageField(upload_to='images/')
    price = models.BigIntegerField()
    certificate = models.FileField(upload_to='certificates/', blank=True, null=True)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES, default='usd')
    description = RichTextField()

    def __str__(self):
        return self.title


class AccomplishedCourse(models.Model):
    profile = models.ForeignKey(Profile,
                                related_name='accomplished_course',
                                on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.title


class Resource(models.Model):
    title = models.CharField(max_length=600)
    file = models.FileField(upload_to='resources/')

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=600)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/')
    video_url = models.URLField()
    resource = models.ManyToManyField(Resource)
    description = RichTextField()

    def __str__(self):
        return self.title


class Like(models.Model):
    profile = models.ForeignKey(Profile, related_name='course_like', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return self.video.title


class Complain(models.Model):
    REASON_CHOICES = (
        ('inappropriate', 'Inappropriate Content'),
        ('spam', 'Spam'),
        ('copyright', 'Copyright Violation'),
        ('other', 'Other'),
    )
    profile = models.ForeignKey(Profile,
                                related_name='course_complain',
                                on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    reason = models.CharField(max_length=20, choices=REASON_CHOICES)
    text = models.TextField()

    def __str__(self):
        return self.video.title


class CommentVideo(BaseModel):
    profile = models.ForeignKey(Profile, related_name='comment_profile', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, related_name='comment_video', on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    text = RichTextField()

    def __str__(self):
        return self.video.title


class CommentCourse(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='comment_course', on_delete=models.CASCADE)
    rate = models.IntegerField(null=True, blank=True)
    text = models.TextField()

    def __str__(self):
        return self.video.title


class VideoWatchProgress(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    last_viewed_seconds = models.PositiveIntegerField()

    def __str__(self):
        return self.video.title
