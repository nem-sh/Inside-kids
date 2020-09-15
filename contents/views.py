from accounts.models import Kid, User

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Video, Paint, Picture, Music, Script, Script, Character
from .serializers import PaintListSerializer, PictureListSerializer, MusicListSerializer, ScriptSerializer


# video


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def video_delete(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    if request.user == video.kid.user:
        video.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=403)
