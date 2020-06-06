from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from useraccount.serializer import UserSerializer,AgentUserSerializer
from rest_framework.views import APIView
from useraccount.models import User
from django.http.response import JsonResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from ticket.models import Organization
import random 
import array

def username_generator(email):
    email = email.split('@')[0]
    return email


def password_generator():
    passwd = ''
    temp_pass_list = []
    MAX_LEN = 12
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                        'z'] 
    
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
                        'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                        'Z'] 
    
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
            '*', '(', ')', '<&# 039;'] 
    
    # combines all the character arrays above to form one array 
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS 
    
    # randomly select at least one character from each character set above 
    rand_digit = random.choice(DIGITS) 
    rand_upper = random.choice(UPCASE_CHARACTERS) 
    rand_lower = random.choice(LOCASE_CHARACTERS) 
    rand_symbol = random.choice(SYMBOLS) 
    
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol 
    
    for x in range(MAX_LEN - 4): 
        temp_pass = temp_pass + random.choice(COMBINED_LIST) 
        temp_pass_list=array.array('&# 039;u&# 039;, temp_pass')
        random.shuffle(temp_pass_list)

    for x in temp_pass_list:
        passwd +=x

    return passwd


class UserModelViewset(ModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    queryset = User.objects.all()

    def create(self,request,*args,**kwargs):
        ser_data = self.get_serializer(data = request.data)
        if ser_data.is_valid():
            org=Organization.objects.create(name = request.data.get('org_name'))
            user = User.objects.create_user(request.data.get('username'), request.data.get('email'),
                request.data.get('password'),is_admin = True,organization = org)
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


class AgentUserViewSet(ModelViewSet):
    serializer_class = AgentUserSerializer
    queryset = User.objects.filter(is_admin = False)

    def create(self,request,*args,**kwargs):
        ser_data = self.get_serializer(data = request.data)
        if ser_data.is_valid():
            email = request.data.get('email')
            username = username_generator(email)
            password = '12345678'
            org = Organization.objects.get(name = request.data.get('org_name'))
            user = User.objects.create_user(username=username,password= password,email = email,organization = org)
            usr_ser = UserSerializer(user)
            token = str(Token.objects.create(user=user))
            return JsonResponse({'token':token,'username':username,'password':password})
        else:
            return JsonResponse(ser_data.errors)













