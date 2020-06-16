from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import serializers
from rest_framework import status , viewsets,filters
from rest_framework.authentication import TokenAuthentication
from profiles_api import models,permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# Create your views here.

class UserInfoViewList(viewsets.ModelViewSet):
    permission_classes = (permissions.permissions.IsAuthenticated,)
    serializer_class = serializers.UserInfoSerializer
    queryset = models.TokoUserInfo.objects.all()

class UserProfileViewSet(viewsets.ModelViewSet):
    """Menghandle membuat dan update profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields=('name','email',)

class UserLoginViewSet(ObtainAuthToken):
    """Handle create user untuk autentikasi token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
