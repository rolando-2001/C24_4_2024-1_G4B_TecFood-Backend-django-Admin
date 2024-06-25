from rest_framework import serializers
from tecfood_admin.models import User
import re

class UserSerializer(serializers.ModelSerializer):
    role_name = serializers.StringRelatedField(source='role.name')
    class Meta:
        model = User
        fields = ['user_id',
                  'first_name',
                  'last_name',
                  'phone_number', 
                  'email', 
                  'password', 
                  'dni', 
                  'username', 
                  'role', 
                  'created_at', 
                  'updated_at',
                  'role_name'
                  
                  ]
        extra_kwargs = {
            'password': {'write_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True}
        }

    def validate_password(self, value):
        # Validar que la contraseña tenga al menos 8 caracteres
        if len(value) < 8:
            raise serializers.ValidationError("La contraseña debe tener al menos 8 caracteres")

        # Validar que la contraseña contenga al menos una letra mayúscula y una minúscula
        if not re.search(r'[A-Z]', value) or not re.search(r'[a-z]', value):
            raise serializers.ValidationError("La contraseña debe contener al menos una letra mayúscula y una minúscula")

        # Validar que la contraseña contenga al menos un carácter especial
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise serializers.ValidationError("La contraseña debe contener al menos un carácter especial")

        return value