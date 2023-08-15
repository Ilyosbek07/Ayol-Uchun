from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.accounts.models import Profile
from apps.accounts.serializers import ProfileSerializer, RegisterUserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.core.mail import send_mail

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.settings import base

from rest_framework_simplejwt.tokens import RefreshToken


class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer


class ProfileRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileListAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]


class ProfileCreateAPIView(generics.CreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
