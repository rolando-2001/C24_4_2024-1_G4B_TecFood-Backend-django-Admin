
####################################################################################################
from tecfood_admin.serializers import LoginSerializer, UserLoginSerializer

####################################################################################################
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

####################################################################################################
from rest_framework import status
from rest_framework.response import Response
from tecfood_admin.models import User




class Login(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
            
        except User.DoesNotExist:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Autenticar al usuario utilizando el nombre de usuario
        user = authenticate(username=user.username, password=password)
       

        if user:
            # Preparar los datos para el serializador de tokens
            data = {'email': email, 'password': password, 'username': user.username}
            
            login_serializer = self.serializer_class(data=data)
            print("login_serializer",login_serializer)
            if login_serializer.is_valid():
                user_serializer = UserLoginSerializer(user)
                
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    
                    'user': user_serializer.data,
                    'message': 'Inicio de sesión exitoso'
                }, status=status.HTTP_200_OK)
            return Response(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)