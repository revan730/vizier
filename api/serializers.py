from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Screenshot


class ScreenDetailSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = Screenshot
        fields = ('id', 'description', 'url')

    def get_url(self, screen):
        return screen.raw.url


class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
