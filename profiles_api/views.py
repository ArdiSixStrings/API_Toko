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

class HelloApiView(APIView):
    """View untuk HelloApiView"""
    serializer_class = serializers.HelloSerializer #class Serializer
    def get(self,request,format=None):
        """Function untuk get data"""
        an_apiview=[
            "Test"
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
        """Function untuk post data"""
        serializer = self.serializer_class(data=request.data) #mengambil serializer class dari variabel diatas
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
                            )

    def put(self,request, pk=None):

        return Response({'method':'PUT'})

    def patch(self,request,pk=None):

        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Function untuk delete data"""
        return Response ({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """View versi viewSet"""
    def list(self,request):
        """Function untuk list data"""
        a_viewset=[
            'Test Viewsets'
        ]
        return Response({'message':'Hello!', 'a_viewset':a_viewset})

    def create(self,request):
        """Function untuk create data"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}!'
            return Response({'message' : message})
        else:
            return Response (
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request,pk=None):

        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Function untuk update data"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):

        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Function untuk menghapus data"""
        return Response({'http_method':'DELETE'})

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
