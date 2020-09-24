from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Kid

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')
        read_only_fields = ('email',)


class KidSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Kid
        fields = '__all__'


class KidListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kid
        fields = ('id', 'name', 'image')
