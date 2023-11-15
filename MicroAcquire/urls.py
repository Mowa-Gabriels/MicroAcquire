"""MicroAcquire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from allauth.socialaccount.views import signup
from authentication.views import GoogleLogin, FacebookLogin
from django.conf import settings
from django.conf.urls.static import static



schema_view = get_schema_view(
   openapi.Info(
      title="Acquire Auth API",
      default_version='v2',
      description="Test Authentication",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@auth.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/v1/', include('authentication.urls')),
    path('marketplace/v1/', include('marketplace.urls')),
    path('token-pass/', include('drfpasswordless.urls')),
    path('dj-rest-auth/v1/', include('dj_rest_auth.urls')),
    # path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    
    
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path("auth/v1/google/", GoogleLogin.as_view(), name="google_login"),
    # path('auth/v1/facebook/', FacebookLogin.as_view(), name='fb_login'),

    path('admin_tools_stats/', include('admin_tools_stats.urls'))
   
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

