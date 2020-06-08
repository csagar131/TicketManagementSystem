from django.db import models
from django.contrib.auth.models import AbstractUser
from ticket.models import Organization


class User(AbstractUser):
    email = models.EmailField(unique = True)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE,related_name = 'org')
    image =  models.ImageField(upload_to ='profiles/',blank = True)
    is_admin = models.BooleanField(default = False)




class Ticket(models.Model):
    curr_status = [
        ('new','New'),('inprocess','InProcess'),('resolved','Resolved')
    ]
    priority_list = [
        ('low','Low'),('medium','Medium'),('high','High'),('urgent','Urgent'),
    ]
    subject = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    status = models.CharField(choices = curr_status,max_length=50)
    priority = models.CharField(choices = priority_list,max_length = 50)
    contact = models.EmailField()
    assignto = models.ForeignKey(User,on_delete=models.CASCADE)
    createdby = models.ForeignKey(User,on_delete= models.CASCADE,related_name = 'creator')
    creationdate = models.DateTimeField(auto_now_add=True)
    updationdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject