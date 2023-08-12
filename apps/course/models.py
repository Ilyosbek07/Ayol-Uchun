from ckeditor.fields import RichTextField
from django.db import models
from apps.common.models import BaseModel
from apps.accounts.models import Profile

class Author(models.Model):
    name = models.CharField(max_length=300)
class Category(models.Model):
    name = models.CharField(max_length=300)
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
    author = models.ManyToManyField(Author)
    title = models.CharField(max_length=600)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    is_recommended = models.BooleanField(default=False)
    is_bestseller = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')
    price = models.BigIntegerField()
    is_active = models.BooleanField(default=True)
    certificate = models.FileField(upload_to='certificates/', blank=True, null=True)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES, default='usd')
    description = RichTextField()

    def __str__(self):
        return self.title

class CommentCourse(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='comment_course', on_delete=models.CASCADE)
    rate = models.IntegerField(null=True, blank=True)
    text = models.TextField()

    class Meta:
        unique_together = ('profile', 'course')

    def __str__(self):
        return self.course.name

class Unit(models.Model):
    title = models.CharField(max_length=600)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)


    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title



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
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class CommentVideo(BaseModel):
    profile = models.ForeignKey(Profile, related_name='comment_profile', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, related_name='comment_video', on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    text = RichTextField()

    def __str__(self):
        return self.text

class VideoWatchProgress(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    last_viewed_seconds = models.PositiveIntegerField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.video.title



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





class UserCourse(models.Model):
    profile = models.ForeignKey(Profile,
                                related_name='accomplished_course',
                                on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_finished = models.BooleanField(default=False)

    class Meta:
        unique_together = ('profile', 'course')

    def __str__(self):
        return self.course.title


class UserCertificate(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    certificate = models.FileField()

    class Meta:
        unique_together = ('profile', 'course')

    def __str__(self):
        return self.course.title
