from rest_framework import serializers
from django.contrib.auth.models import User

from home.models import Friend


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class FriendSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Friend
        fields = ('id', 'fb_id', 'full_name', 'photo')

