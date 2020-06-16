from rest_framework import serializers
from profiles_api import models

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

class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.TokoUserInfo
        fields=('id','nama_pemilik','alamat','nama_toko','kode_pos','latitude','longtitude','photo')
