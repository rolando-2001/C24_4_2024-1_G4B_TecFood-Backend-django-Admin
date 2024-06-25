from rest_framework import viewsets
from tecfood_dish.models import Dish
from tecfood_dish.serializers import DishSerializer
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.http import Http404

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name', 'price']  
    ordering = ['name']  # Ordenamiento por defecto

    def list(self, request):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            page=self.paginate_queryset(queryset)
            if page is not None:
                serializer=self.get_serializer(page, many=True)
                
                return self.get_paginated_response(serializer.data)    
            serializer=self.get_serializer(queryset, many=True)
            
            return Response({'dish':serializer.data},
                            status=status.HTTP_200_OK
                            ) 
            
        
        except Exception as e:
            return Response(
                            {'error': str(e)}, 
                            status=status.HTTP_400_BAD_REQUEST)
            


    def create(self, request):
            try:
                disd_data = request.data
                print(disd_data)
                serializer = self.get_serializer(data=disd_data)
                serializer.is_valid(raise_exception=True)  # Lanza una excepción si no es válido
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(
                    {'dish':serializer.data},
                    status=status.HTTP_201_CREATED,
                    headers=headers
                )

            except Exception as e:
                return Response(
                    {'error': str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )
            

    def update(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.serializer_class(instance, data=request.data)

            if serializer.is_valid(raise_exception=True):
                self.perform_update(serializer)
                return Response(
                    {
                        'message': 'Registro actualizado',
                        'dish': serializer.data['name']
                    },
                    status=status.HTTP_200_OK
                )
        except Http404:
            return Response(
                            {'error': 'No se encontró el registro'},
                            status=status.HTTP_404_NOT_FOUND
                           )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

        
    def destroy(self, request, pk=None):
        try:
            instance = self.get_object()
            if instance:
                self.perform_destroy(instance)
                return Response(
                               {'message': 'Registro eliminado'},
                                 status=status.HTTP_200_OK)
        except Http404:
            return Response(
                           {'error': 'No se encontró el registro'},
                           status=status.HTTP_404_NOT_FOUND
                           )
            
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
         