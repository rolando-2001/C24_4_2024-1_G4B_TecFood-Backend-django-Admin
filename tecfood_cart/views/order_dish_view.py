from rest_framework import viewsets
from tecfood_cart.models import OrderDish
from tecfood_cart.serializers import OrderDishSerializer
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
class OrderDishViewSet(viewsets.ModelViewSet):
    queryset = OrderDish.objects.all()
    serializer_class = OrderDishSerializer
 
    


    def list(self, request):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(queryset, many=True)
            return Response({'order': serializer.data},
                            status=status.HTTP_200_OK)
        except Http404:
            return Response(
                {'message': 'error al listar las ordenes'},
                status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            order_data = request.data
            print(order_data)
            serializer = self.get_serializer(data=order_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                {'order': serializer.data},
                status=status.HTTP_201_CREATED,
                headers=headers)
        except Http404:
            return Response(
                {'message': 'error al crear la orden'},
                status=status.HTTP_400_BAD_REQUEST
            )
    def update(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({'order': serializer.data},
                            status=status.HTTP_200_OK)
        except Http404:
            return Response(
                {'message': 'error al actualizar la orden'},
                status=status.HTTP_400_BAD_REQUEST
            )
    def destroy(self, request, pk=None):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(
                {'message': 'orden eliminada'},
                status=status.HTTP_204_NO_CONTENT
            )
        except Http404:
            return Response(
                {'message': 'error al eliminar la orden'},
                status=status.HTTP_400_BAD_REQUEST
            )