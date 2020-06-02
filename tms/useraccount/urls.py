from django.urls import path,include
from rest_framework.routers import DefaultRouter
from useraccount.views import UserCreateViewSet

user_router = DefaultRouter()
user_router.register('user',UserCreateViewSet)


urlpatterns = [
    path('',include(user_router.urls)),
]