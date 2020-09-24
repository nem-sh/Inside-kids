from django.urls import path
from . import views

app_name = 'contents'

urlpatterns = [


    # video
    path('videos/<int:video_id>/', views.video_delete),
    path('kids/<int:kid_id>/videos/', views.video_create),

    # paint
    path('kids/<int:kid_id>/paints/', views.paint_list_or_create),
    path('paints/<int:paint_id>/', views.paint_delete),

    # picture
    path('kids/<int:kid_id>/pictures/', views.picture_list_or_create),
    path('pictures/<picture_id>/', views.picture_delete),

    # music
    path('musics/', views.music_list),

    # script
    path('kids/<int:kid_id>/scripts/', views.script_create),
    path('scripts/<int:script_id>/', views.script_delete),

    # character
    path('characters/<character_id>/', views.character_detail_or_update),



]
