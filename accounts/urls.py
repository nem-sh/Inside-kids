from django.urls import path
from . import views

urlpatterns = [
    path('delete/', views.delete),
    path('kids/', views.kid_create_or_list),
    path('kids/<int:kid_id>/', views.kid_detail_or_update_or_delete),
    path('google/', views.GoogleLogin.as_view()),
]
