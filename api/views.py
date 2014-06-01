from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers, permissions, authenticators
from rest_framework import viewsets
from .serializers import UserSerializer, FriendSerializer
from django.contrib.auth import login, logout

from home.models import Friend


# API Rest for User
class UserViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer
    filter_fields = ('id', 'first_name', 'last_name', )


# API Rest for Friends
class FriendViewSet(viewsets.ModelViewSet):
    model = Friend
    serializer_class = FriendSerializer
    filter_fields = ('id', 'fb_id', 'full_name', )


# API Rest for Auth
class AuthView(APIView):
    authentication_classes = (authenticators.QuietBasicAuthentication,)

    def post(self, request, *args, **kwargs):
        login(request, request.user)
        return Response(serializers.UserSerializer(request.user).data)

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response()