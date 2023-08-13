from django.db import models
from django.contrib.auth.models import User

from apps.common.models import BaseModel


class Country(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Position(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Region(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Profile(BaseModel):
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    occupation = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    desc = models.TextField()
    mail_index = models.IntegerField()
    is_email_verified = models.BooleanField(default=False)
    instagram_url = models.URLField(null=True, blank=True)
    imkon_url = models.URLField(null=True, blank=True)
    linked_in_url = models.URLField(null=True, blank=True)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    country = models.ForeignKey(
        Country, related_name="country_profiles", on_delete=models.CASCADE
    )
    region = models.ForeignKey(
        Region, related_name="region_profiles", on_delete=models.CASCADE
    )
    position = models.ForeignKey(
        Position, related_name="position_profiles", on_delete=models.CASCADE
    )
    birthdate = models.DateTimeField()

    def __str__(self):
        return self.user.username + "'s Profile"


class PaymentType(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Payment(BaseModel):
    status = models.BooleanField(default=False)
    payment_type = models.ForeignKey(
        PaymentType, related_name="payment_type_payments", on_delete=models.CASCADE
    )
    # course = models.ForeignKey(Course, related_name='course_payments', on_delete=models.CASCADE)


class PaymentProcess(BaseModel):
    fullname = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16)
    expiry_date = models.IntegerField()
    cvv = models.IntegerField()

    def __str__(self):
        return self.fullname + "'s Profile Payment"
