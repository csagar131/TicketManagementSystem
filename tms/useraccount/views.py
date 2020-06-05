from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from useraccount.serializer import SignupUserSerializer
from rest_framework.views import APIView
from useraccount.models import User
from django.http.response import JsonResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from ticket.models import Organization


class UserModelViewset(ModelViewSet):
    serializer_class = SignupUserSerializer
    authentication_classes = [TokenAuthentication]
    queryset = User.objects.all()

    def create(self,request,*args,**kwargs):
        ser_data = self.get_serializer(data = request.data)
        if ser_data.is_valid():
            user = User.objects.create_user(request.data.get('username'), request.data.get('email'),
                request.data.get('password'),is_admin = True,org_name = request.data.get('org_name'))
            usr = request.data['username']
            msg_html = render_to_string('email_template.html',{'usr':usr})
            send_mail('Subject here','Here is the message.','chouhansagar131@gmail.com',
                    [request.data['email'],'chouhansagar131@gmail.com'],html_message=msg_html,
                    fail_silently=False,
            )
            token = str(Token.objects.create(user=user))
            return JsonResponse({'token':token,'user':ser_data.data})
        else:
            return JsonResponse(ser_data.errors)


class AgentCreateAPIView(APIView):
    def post(self,request,*args,**kwargs):
        pass










