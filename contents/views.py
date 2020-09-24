from accounts.models import Kid, User

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Video, Paint, Picture, Music, Script, Character
from .serializers import VideoSerializer, PaintSerializer, PaintListSerializer, PictureSerializer, PictureListSerializer, MusicListSerializer, ScriptSerializer, CharacterSerializer


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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def video_create(request, kid_id):
    kid = get_object_or_404(Kid, pk=kid_id)
    serializer = VideoSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(kid=kid)
        return Response(serializer.data)
    else:
        return HttpResponse(status=400)


# paint


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def paint_list(request, kid_id):
    kid = get_object_or_404(Kid, pk=kid_id)
    paints = kid.paint_set.order_by()
    serializer = PaintListSerializer(paints, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def paint_delete(request, paint_id):
    paint = get_object_or_404(Paint, pk=paint_id)

    if request.user == paint.kid.user:
        paint.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=403)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def paint_create(request, kid_id):
    kid = get_object_or_404(Kid, pk=kid_id)
    serializer = PaintSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(kid=kid)
        return Response(serializer.data)
    else:
        return HttpResponse(status=400)


# picture


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def picture_list(request, kid_id):
    kid = get_object_or_404(Kid, pk=kid_id)
    pictures = kid.picture_set.order_by()
    serializer = PictureListSerializer(pictures, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def picture_delete(request, picture_id):
    picture = get_object_or_404(Picture, pk=picture_id)
    if request.user == picture.kid.user:
        picture.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=403)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def picture_create(request, kid_id):
    kid = get_object_or_404(Kid, pk=kid_id)
    serializer = PictureSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(kid=kid)
        return Response(serializer.data)
    else:
        return HttpResponse(status=400)


# music


@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicListSerializer(musics, many=True)
    return Response(serializer.data)


# script


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def script_create(request, kid_id):
    kid = get_object_or_404(Kid, pk=kid_id)
    serializer = ScriptSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(kid=kid)
        return Response(serializer.data)
    else:
        return HttpResponse(status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def script_delete(request, script_id):
    script = get_object_or_404(Script, pk=script_id)
    if request.user == script.kid.user:
        script.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=403)


# character


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def character_detail_or_update(request, character_id):
    character = get_object_or_404(Character, kid_id=character_id)
    if request.method == 'PUT':
        character.eat_time = request.data['eat_time']
        character.wash_time = request.data['wash_time']
        character.save()
    serializer = CharacterSerializer(character)
    return Response(serializer.data)
