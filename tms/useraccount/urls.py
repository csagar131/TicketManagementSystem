from django.urls import path,include
from rest_framework.routers import DefaultRouter
from useraccount.views import UserCreateViewSet

user_router = DefaultRouter(trailing_slash=False)
user_router.register('user',UserCreateViewSet)
user_router.register('signup',UserCreateViewSet)



urlpatterns = [
    path('',include(user_router.urls)),
]