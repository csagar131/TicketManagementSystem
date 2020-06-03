from rest_framework import serializers
from useraccount.models import User
from rest_framework.validators import UniqueValidator
from django.core.mail import send_mail

class SignupUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):        
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])

        send_mail('Subject here','Here is the message.','chouhansagar131@gmail.com',
                [validated_data['email'],'chouhansagar131@gmail.com'],
                fail_silently=False,
        )
        return user

    class Meta:
        model = User
        fields = ('id','username', 'email', 'password')










