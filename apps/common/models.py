from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SocialMedia(BaseModel):
    name = models.CharField(max_length=255)
    link = models.URLField()
    photo = models.ImageField(upload_to='social_media_photos/')

    def __str__(self):
        return self.name


class Notification(BaseModel):
    STATUS_CHOICES = [
        ('moderation', 'Moderation'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name


class UserNotification(BaseModel):
    user = models.ForeignKey(
        User,
        related_name='user_notification',
        on_delete=models.CASCADE
    )
    notification = models.ForeignKey(
        Notification,
        related_name='notification',
        on_delete=models.CASCADE
    )
    is_read = models.BooleanField(default=False)


class Contact(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    text = models.TextField()

    def __str__(self):
        return self.name
