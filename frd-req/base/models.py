from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email=models.EmailField(null=True)
    friendreq=models.ManyToManyField("User",blank=True)
    REQUIRED_FIELDS=[]
    
    def __str__(self):
        return self.username
    
class Friend_request(models.Model):
    from_user=models.ForeignKey(User,related_name="from_user",on_delete=models.CASCADE)
    to_user=models.ForeignKey(User,related_name="to_user",on_delete=models.CASCADE)
    

class Post(models.Model):
    host=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    comments=models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    