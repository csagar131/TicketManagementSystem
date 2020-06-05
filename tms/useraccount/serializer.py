from rest_framework import serializers
from useraccount.models import User
from rest_framework.validators import UniqueValidator
from django.core.mail import send_mail
from django.template.loader import render_to_string


class SignupUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8)
    
    org_name = serializers.CharField(max_length = 255)

    class Meta:
        model = User
        fields = ('id','username', 'email', 'password','org_name','is_author')










