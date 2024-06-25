from django.urls import path
from rest_framework.routers import DefaultRouter

from tecfood_cart.views import OrderDishViewSet

router = DefaultRouter()
router.register(r'order-dish', OrderDishViewSet)

urlpatterns = router.urls