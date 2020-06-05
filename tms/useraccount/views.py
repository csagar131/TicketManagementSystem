from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from useraccount.serializer import SignupUserSerializer
from useraccount.models import User
from django.http.response import JsonResponse
from rest_framework.generics import CreateAPIView
from django.template.loader import render_to_string
from django.core.mail import send_mail
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication


class UserModelViewset(ModelViewSet):
    serializer_class = SignupUserSerializer
    authentication_classes = [TokenAuthentication]
    queryset = User.objects.all()
    # permission_classes = (IsAuthenticated,)


    def create(self,request,*args,**kwargs):
        print(self.request.data)
        user = User.objects.create_user(request.data['username'], request.data['email'],
             request.data['password'])
        usr = request.data['username']
        msg_html = render_to_string('email_template.html',{'usr':usr})
        send_mail('Subject here','Here is the message.','chouhansagar131@gmail.com',
                [request.data['email'],'chouhansagar131@gmail.com'],html_message=msg_html,
                fail_silently=False,
        )
        token = str(Token.objects.create(user=user))
        return JsonResponse({'token':token})





