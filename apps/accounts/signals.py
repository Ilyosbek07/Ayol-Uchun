import passgenerator
from django.contrib.auth.models import User

# from .models import SendRequest_to_login, Doctor_Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.mail import send_mail

from core.settings import base


# @receiver(post_save, sender=User)
# def create_auth_user(sender, instance=None, created=False, **kwargs):
#     if created:
#         password = passgenerator.generate()
#
#         send_verification_to_user_email(
#             email=instance.email,
#             username=instance.user.username,
#             password=password
#         )


def send_verification_to_user_email(email, username, password):
    subject = 'Verification Code from Web-Site\n\n'
    message = f"Your verification code is - {password} and your username is - {username} you can login into your account "
    from_email = base.EMAIL_HOST_USER
    send_mail(
        subject,
        message,
        from_email,
        [email],
        fail_silently=False,
    )
