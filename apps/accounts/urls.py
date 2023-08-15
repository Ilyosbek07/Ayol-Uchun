from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
from apps.accounts.views import (
    ProfileCreateAPIView,
    ProfileUpdateAPIView,
    ProfileRetrieveAPIView, ProfileListAPIView, RegistrationView
)

urlpatterns = [
    path('list/', ProfileListAPIView.as_view(), name='profile-list'),
    path('create/', ProfileCreateAPIView.as_view(), name='profile-create'),
    path('update/<int:pk>/', ProfileUpdateAPIView.as_view(), name='profile-update'),
    path('detail/<int:pk>/', ProfileRetrieveAPIView.as_view(), name='profile-detail'),

    # JWT
    path('api/register/', RegistrationView.as_view(), name='jwt_register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
