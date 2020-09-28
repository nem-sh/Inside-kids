from django.urls import path, include
from rest_auth import views

urlpatterns = [
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
]
