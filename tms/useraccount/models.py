from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique = True)
    org_name = models.CharField(max_length = 255)
    image =  models.ImageField(upload_to ='profiles/',blank = True)
    is_admin = models.BooleanField(default = False)