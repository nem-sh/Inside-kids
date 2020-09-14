from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Kid
from .serializers import KidSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = KidSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response({"status": "OK", **serializer.data})
