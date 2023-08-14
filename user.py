from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import SET_NULL, TextChoices

from django.utils.translation import ngettext_lazy as _

# from users.models.abstract_user import AbstractUser, UserManager, BaseUserManager

phone_regex = RegexValidator(
    regex=r'^998[0-9]{9}$',
    message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed."
)


class CustomUserManager(BaseUserManager):

    def create_user(self, username, password, **extra_fields):

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, password, **extra_fields)


class User(AbstractUser):
    DARK = 'dark'
    LIGHT = 'light'
    THEMES_CHOICES = (
        (DARK, 'Dark'),
        (LIGHT, 'Light'),
    )
    UZ = 'uz'
    OZ = 'oz'
    RU = 'ru'

    LANGUAGES_CHOICES = (
        ('uz', 'Lotin'),
        ('oz', 'Uzbek'),
        ('ru', 'Russian'),
    )
    username = models.CharField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=12, validators=[phone_regex], blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    language = models.CharField(max_length=25, choices=LANGUAGES_CHOICES, blank=True, null=True)
    theme = models.CharField(max_length=24, choices=THEMES_CHOICES, default=DARK, blank=True, null=True)

    # mac_address = models.JSONField(default=dict, null=True, blank=True)
    photo = models.ImageField(upload_to="users/images/", blank=True, null=True)
    role = models.ManyToManyField("users.Role", through='users.UserRole')

    is_validated = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    objects = CustomUserManager()

    def __str__(self):
        return self.username

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['-id']


# j3QQ4HHH7777@
# ssh -L 1111:localhost:5432 root@dicore.uz -N -p 48822

