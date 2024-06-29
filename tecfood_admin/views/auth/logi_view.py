
####################################################################################################
from tecfood_admin.serializers import LoginSerializer, UserLoginSerializer

####################################################################################################
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

####################################################################################################
from rest_framework import status
from rest_framework.response import Response
from tecfood_admin.models import User,Role




class Login(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
            role=user.role
            print("role#####",role)
            
        except User.DoesNotExist:
            return Response({'message': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Autenticar al usuario utilizando el nombre de usuario
        #role =Role.objects.get(role_id=user.role_id)


        user = authenticate(username=user.username, password=password)
           
    
        if user and role.name == 'ROLE_ADMIN':
            # Preparar los datos para el serializador de tokens
            data = {'email': email, 'password': password, 'username': user.username}
            
            login_serializer = self.serializer_class(data=data)
           
            if login_serializer.is_valid():
                user_serializer = UserLoginSerializer(user)
                
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    
                    'user': user_serializer.data,
                    'message': 'Inicio de sesión exitoso'
                }, status=status.HTTP_200_OK)
            return Response(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif user and role.name != 'ROLE_ADMIN':
            return Response({'message': 'Usted no es un administrador'}, status=status.HTTP_403_FORBIDDEN)

        
        return Response({'message': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)