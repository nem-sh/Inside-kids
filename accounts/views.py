from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Kid
from .serializers import KidSerializer, KidListSerializer


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


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def kid_detail_or_update(request, kid_id):
    kid = get_object_or_404(Kid, id=kid_id)
    if request.method == 'GET':
        serializer = KidSerializer(kid)
        return Response(serializer.data)
    else:
        serializer = KidSerializer(kid, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
