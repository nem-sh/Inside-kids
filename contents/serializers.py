from rest_framework import serializers
from .models import Video, Paint, Picture, Music, Script, Character


class PaintListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paint
        fields = ('created_at', 'file_source')


class PictureListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Picture
        fields = ('created_at', 'file_source')


class MusicListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ('title', 'file_source')
