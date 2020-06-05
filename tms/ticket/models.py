from django.db import models
from useraccount.models import User
# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length = 255)
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    agent = models.ForeignKey(User,on_delete=models.CASCADE,related_name='agent')