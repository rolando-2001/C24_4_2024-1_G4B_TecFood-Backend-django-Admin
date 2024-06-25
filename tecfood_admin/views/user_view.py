from rest_framework import viewsets
from rest_framework.response import Response
from tecfood_admin.models import User
from tecfood_admin.serializers import UserSerializer
from rest_framework import status
import datetime

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                user.username = user.first_name
                user.created_at = datetime.datetime.now()
                user.updated_at = datetime.datetime.now()
                user.set_password(request.data['password'])
                user.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    def list(self, request):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    def retrieve(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    def update(self, request, pk=None):
        user_dat=request.data
        print(user_dat)
        try:
            instance =self.get_object()
            serializer = UserSerializer(instance, data=user_dat, partial=True)
            if serializer.is_valid():
                user = serializer.save()
                user.username = user.first_name
                user.updated_at = datetime.datetime.now()
                user.set_password(request.data['password'])
                user.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    def destroy(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response(status=204)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)