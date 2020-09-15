"""backend URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_auth import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # rest-auth
    path('accounts/', include('rest_auth.urls')),
    path('accounts/signup/', include('rest_auth.registration.urls')),
    path('accounts/password/reset/',
         views.PasswordResetView.as_view(), name="password_reset"),
    path('accounts/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),


    # app
    path('accounts/', include('accounts.urls')),
    path('contents/', include('contents.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
