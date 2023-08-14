from django.urls import path

from apps.accounts.views import (
    logout_view,
    ProfileCreateAPIView,
    ProfileUpdateAPIView,

)

urlpatterns = [
    # When user logut user token deleted
    path('logout/', logout_view, name='logout'),
    path('create/', ProfileCreateAPIView.as_view(), name='profile-create'),
    path('update/<int:pk>/', ProfileUpdateAPIView.as_view(), name='profile-update'),
    path('detail/<int:pk>/', ProfileCreateAPIView.as_view(), name='profile-detail'),
]
