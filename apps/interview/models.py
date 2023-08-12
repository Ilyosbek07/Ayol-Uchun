from django.db import models
from apps.accounts.models import Profile
from apps.blog.models import Blog
from apps.common.models import BaseModel
from phonenumber_field.modelfields import PhoneNumberField
#######

class Interview(BaseModel):
    profile = models.ForeignKey(Profile, related_name='interviews', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='interview_videos/')
    url = models.URLField()
    thumbnail = models.ImageField(upload_to='interview_thumbnails/')
    description = models.TextField()

    def __str__(self):
        return self.title
