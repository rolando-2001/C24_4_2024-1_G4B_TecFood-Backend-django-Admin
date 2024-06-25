from django.urls import path
from rest_framework.routers import DefaultRouter

from tecfood_dish.views import DishViewSet, DishCategoryViewSet

router = DefaultRouter()
router.register(r'dish', DishViewSet)
router.register(r'dish-category', DishCategoryViewSet)

urlpatterns = router.urls



