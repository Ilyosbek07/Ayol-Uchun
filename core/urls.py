from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .schema import swagger_urlpatterns
from rest_framework.authtoken import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("course/", include("apps.course.urls")),
    path('api-token-auth/', views.obtain_auth_token)

]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
