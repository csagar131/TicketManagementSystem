from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from useraccount.serializer import SignupUserSerializer
from useraccount.models import User



class UserCreateViewSet(ModelViewSet):
    serializer_class = SignupUserSerializer
    queryset = User.objects.all()


