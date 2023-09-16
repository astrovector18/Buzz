from django.db import models
from django.contrib.auth.models import User 
# Create your models here. 

class Post(models.Model): 
  author = models.ForeignKey(User , on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  body = models.TextField()
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True) 
  class Meta:
    ordering = ['-created','-updated']
  def __str__(self):
    return self.body [:50] 
    
class Profile(models.Model):
  bio = models.CharField(max_length=40) 
  owner = models.OneToOneField(User,on_delete= models.CASCADE) 
  image = models.ImageField(default='default.jpg', upload_to='profile_pics') 
  
  def __str__(self):
    return ( f"{self.owner.username} Profile.")