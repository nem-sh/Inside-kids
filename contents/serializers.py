from rest_framework import serializers
from .models import Video, Paint, Picture, Music, Script, Character

# video


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ('file_source',)

# paint


class PaintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paint
        fields = ('file_source',)


class PaintListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paint
        fields = ('created_at', 'file_source')

# picture


class PictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Picture
        fields = ('file_source',)


class PictureListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Picture
        fields = ('created_at', 'file_source')

# music


class MusicListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ('title', 'file_source')

# script


class ScriptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Script
        fields = ('created_at', 'file_source')

# character


class CharacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character
        fields = ('eat_time', 'wash_time')
