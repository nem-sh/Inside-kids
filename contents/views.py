from accounts.models import Kid, User

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Video, Paint, Picture, Music, Script, Character
from .serializers import VideoSerializer, PaintSerializer, PaintListSerializer, PictureSerializer, PictureListSerializer, MusicListSerializer, ScriptSerializer, ScriptCreateSerializer, CharacterSerializer

import random

# from .tts.infer import save_wav
# video
from .lie_detector import lie_detector

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
def video_create(request, kid_id, script_id):
    kid = get_object_or_404(Kid, pk=kid_id)
    script = get_object_or_404(Script, pk=script_id)
    script.state = 1
    script.save()
    serializer = VideoSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(kid=kid, script=script)
        return Response(serializer.data)
    else:
        return HttpResponse(status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def video_analysis(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    path = video.file_source
    res = lie_detector.get('media/'+str(path))
    if res['true']==0 and res['lie']==0:
        video.analysis = 'nature'
    elif res['true']<res['lie']:
        video.analysis = 'lie'
    else:
        video.analysis = 'true'

    video.save()
    
    return Response({'status':'ok'})
# paint


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def paint_list_or_create(request, kid_id):
    kid = get_object_or_404(Kid, pk=kid_id)
    if request.user == kid.user:
        if request.method == 'GET':
            paints = kid.paint_set.order_by()
            serializer = PaintListSerializer(paints, many=True)
            return Response(serializer.data)
        else:
            serializer = PaintSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(kid=kid)
                return Response(serializer.data)
            else:
                return HttpResponse(status=400)
    else:
        return HttpResponse(status=403)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def paint_delete(request, paint_id):
    paint = get_object_or_404(Paint, pk=paint_id)

    if request.user == paint.kid.user:
        paint.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=403)


# picture


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def picture_list_or_create(request, kid_id):
    kid = get_object_or_404(Kid, pk=kid_id)
    if request.user == kid.user:
        if request.method == 'GET':
            pictures = kid.picture_set.order_by()
            serializer = PictureListSerializer(pictures, many=True)
            return Response(serializer.data)
        else:
            serializer = PictureSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(kid=kid)
                return Response(serializer.data)
            else:
                return HttpResponse(status=400)
    else:
        return HttpResponse(status=403)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def picture_delete(request, picture_id):
    picture = get_object_or_404(Picture, pk=picture_id)
    if request.user == picture.kid.user:
        picture.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=403)

# music


@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicListSerializer(musics, many=True)
    return Response(serializer.data)


# script


@api_view(['POST', 'GET'])
# @permission_classes([IsAuthenticated])
def script_list_or_create(request, kid_id):
    kid = get_object_or_404(Kid, pk=kid_id)
    if request.user == kid.user:
        if request.method == 'GET':
            scripts = Script.objects.filter(kid_id=kid_id, state=0)
            n = scripts.count()
            serializer = ScriptSerializer(scripts, many=True)
            random_scripts = Script.objects.filter(state=2)
            random_serializer = ScriptSerializer(random_scripts, many=True)
            response_data = random.sample(
                random_serializer.data, 5-n) + serializer.data
            return Response(response_data)
        else:
            serializer = ScriptCreateSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                script = serializer.save(kid=kid)
                # save_wav(script.content, str(script.id))
                return Response(serializer.data)
            else:
                return HttpResponse(status=400)
    else:
        return HttpResponse(status=403)


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
def character_detail_or_update(request, kid_id):
    character = get_object_or_404(Character, kid_id=kid_id)
    kid = get_object_or_404(Kid, id=character.kid_id)
    if request.user == kid.user:
        if request.method == 'PUT':
            character.eat_time = request.data['eat_time']
            character.wash_time = request.data['wash_time']
            character.save()
            serializer = CharacterSerializer(character)
            return Response(serializer.data)
        else:
            if Script.objects.filter(kid_id=kid_id, state=0).exists():
                exist_talk = True
            else:
                exist_talk = False
            serializer = CharacterSerializer(character)
            return Response({**serializer.data, **{"exist_talk": exist_talk}})
    else:
        return HttpResponse(status=403)
