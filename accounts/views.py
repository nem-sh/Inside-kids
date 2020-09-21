from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


from .models import Kid
from .serializers import KidSerializer, KidListSerializer

from contents.models import Paint, Video, Picture
from contents.serializers import PaintListSerializer, VideoSerializer, PictureListSerializer


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request):
    request.user.delete()
    return Response({'status': 'success'})


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def kid_create_or_list(request):
    if request.method == 'POST':
        serializer = KidSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)

    else:
        kids = Kid.objects.filter(user=request.user)
        serializer = KidListSerializer(kids, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def kid_detail_or_update_or_delete(request, kid_id):
    kid = get_object_or_404(Kid, id=kid_id)
    if request.method == 'GET':
        paint_serializer = PaintListSerializer(
            Paint.objects.filter(kid=kid),
            many=True
        )
        video_serializer = VideoSerializer(
            Video.objects.filter(kid=kid),
            many=True
        )
        picture_serializer = PictureListSerializer(
            Picture.objects.filter(kid=kid),
            many=True
        )
        serializer = KidSerializer(kid)

        return Response(
            {
                **serializer.data,
                "paints": paint_serializer.data,
                "videos": video_serializer.data,
                "pictures": picture_serializer.data
            }
        )

    elif request.method == 'PUT':
        serializer = KidSerializer(kid, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        kid.delete()
        return Response({'status': 'success'})


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
