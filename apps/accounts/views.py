from rest_framework import generics
from rest_framework.response import Response

from apps.accounts.models import Profile
from apps.accounts.serializers import ProfileSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.core.mail import send_mail

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from djoser import utils

from core.settings import base


@api_view(['POST', ])
def logout_view(request):
    # First
    try:
        token = Token.objects.get(user=request.user)
        print(token)
        token.delete()
        return Response({
            "Response": "Token deleted"
        })
    except Exception as err:
        return Response({
            "Erorr": f"{err}"
        })


class ProfileRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileCreateAPIView(generics.CreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


