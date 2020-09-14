from django.urls import path
from . import views

urlpatterns = [
    path('kids/', views.kid_create_or_list)
]
