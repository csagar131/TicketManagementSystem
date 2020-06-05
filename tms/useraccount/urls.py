from django.urls import path,include
from rest_framework.routers import DefaultRouter
from useraccount.views import UserModelViewset
from django.contrib.auth.views import LoginView

user_router = DefaultRouter(trailing_slash=False)
user_router.register('user',UserModelViewset)
user_router.register('signup',UserModelViewset)



urlpatterns = [
    path('',include(user_router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
]