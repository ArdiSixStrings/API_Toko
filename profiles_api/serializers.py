from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializer sama kan data nya dengan models"""
    name=serializers.CharField(max_length=30)

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.UserProfile
        fields=('id','email','name','password')
        extra_kwargs= {
            'password':
                {
                    'write_only':True,
                    'style' : {'input_type':'password'}
                }
        }

    def create(self,validated_data):
        """OVeride function create dari models"""
        users=models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )

        return users

