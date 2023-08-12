from rest_framework import serializers

from apps.accounts.models import Profile, PaymentType, PaymentProcess, Payment


class ProfileSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

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


class PaymentTypeSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = PaymentType
        fields = (
            'name',
            'created_at',
            'updated_at',
        )


class PaymentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Payment
        fields = (
            'status',
            'payment_type',
            'created_at',
            'updated_at',
        )


class PaymentProcessSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

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
