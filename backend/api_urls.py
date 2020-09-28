from django.urls import path, include, re_path
from rest_auth import views
from django.conf import settings
from django.conf.urls.static import static
from rest_auth.registration.views import VerifyEmailView
from accounts import views as accounts_views

urlpatterns = [
    # rest-auth
    path('accounts/', include('rest_auth.urls')),
    path('accounts/signup/account-confirm-email/<key>/',
         accounts_views.email_verification,
         name="account_confirm_email"),
    path('accounts/signup/', include('rest_auth.registration.urls')),
    re_path(r'^account-confirm-email/', VerifyEmailView.as_view(),
            name='account_email_verification_sent'),
    path('accounts/password/reset/',
         views.PasswordResetView.as_view(), name="password_reset"),
    re_path(r'accounts/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # app
    path('accounts/', include('accounts.urls')),
    path('contents/', include('contents.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
