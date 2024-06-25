from django.urls import path,include
from rest_framework.routers import DefaultRouter

###################################################
from tecfood_admin.views.auth import Login
from tecfood_admin.views.auth import CustomTokenVerifyView
from tecfood_admin.views import UserViewSet
###################################################


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    #url for admin
    path('', include(router.urls) ),

    #url for auth
    path('login/', Login.as_view(), name='login'),
    path('verify/', CustomTokenVerifyView.as_view(), name='token'),

]