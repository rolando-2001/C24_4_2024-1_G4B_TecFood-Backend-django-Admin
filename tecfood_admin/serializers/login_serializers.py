from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from tecfood_admin.models import User




class LoginSerializer(TokenObtainPairSerializer):
    pass




    
class UserLoginSerializer(serializers.ModelSerializer):
    role_name = serializers.StringRelatedField(source='role.name')
    class Meta:
        model = User
        fields = [
            'user_id',
            'username',
            'email',
            'role_name',
        ]
