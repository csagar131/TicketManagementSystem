from django.db import models
from django.contrib.auth.models import AbstractUser
from ticket.models import Organization


class User(AbstractUser):
    email = models.EmailField(unique = True)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE,related_name = 'org')
    image =  models.ImageField(upload_to ='profiles/',blank = True)
    is_admin = models.BooleanField(default = False)