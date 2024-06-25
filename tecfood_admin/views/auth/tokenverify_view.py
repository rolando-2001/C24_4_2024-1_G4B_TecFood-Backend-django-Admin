from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from tecfood_admin.models import User
from tecfood_admin.serializers import UserSerializer
from rest_framework_simplejwt.tokens import UntypedToken, TokenError
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

class CustomTokenVerifyView(APIView):
    
    def post(self, request, *args, **kwargs):
        token = request.data.get('token')

        if not token:
            return Response({'error': 'Token no proporcionado'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Decodifica el token
            decoded_token = UntypedToken(token)

            # Obtiene el ID del usuario del token decodificado
            user_id = decoded_token['user_id']

            # Obtiene el usuario con el ID del token
            user = User.objects.get(pk=user_id)
            
            # Serializa el usuario
            user_serializer = UserSerializer(user)

            # Genera un nuevo par de tokens
            token_serializer = TokenObtainPairSerializer()
            tokens = token_serializer.get_token(user)
            
            # Devuelve la respuesta con los datos del usuario y los tokens
            return Response({
                'user': user_serializer.data,
                'token': str(tokens.access_token),
            })

        except TokenError as e:
            return Response({'error': 'Token inválido o expirado'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
