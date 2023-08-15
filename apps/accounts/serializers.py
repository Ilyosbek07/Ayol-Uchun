from rest_framework import serializers
from django.contrib.auth.models import User
from apps.accounts.models import Profile, PaymentType, PaymentProcess, Payment, Position, Country, Region
# serializers.py

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterUserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "email",
            'token'
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "token": {"read_only": True},
        }

    def get_token(self, user):
        tokens = RefreshToken.for_user(user)
        data = {"refresh": str(tokens), "access": str(tokens.access_token)}
        return data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'user',
            'occupation',
            'gender',
            'desc',
            'mail_index',
            'is_email_verified',
            'instagram_url',
            'imkon_url',
            'linked_in_url',
            'country',
            'position',
            'region',
            'birthdate',
            'created_at',
            'updated_at',
        )


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = (
            'name',
            'created_at',
            'updated_at',
        )


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'name',
            'created_at',
            'updated_at',
        )


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = (
            'name',
            'created_at',
            'updated_at',
        )


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = (
            'name',
            'created_at',
            'updated_at',
        )


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'status',
            'payment_type',
            'created_at',
            'updated_at',
        )


class PaymentProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentProcess
        fields = (
            'fullname',
            'card_number',
            'expiry_date',
            'cvv',
            'created_at',
            'updated_at',
        )
