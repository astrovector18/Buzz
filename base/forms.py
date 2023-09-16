from django.forms import ModelForm 
from django.contrib.auth.models import User 
## import the Room class from models.py 

from .models import Post,Profile 

class CreatePostForm(ModelForm):
  class Meta: 
    model = Post
    fields = '__all__' 
    exclude = ['author'] 
    
class UserUpdateForm(ModelForm):
  class Meta:
    model = User 
    fields = [ 'username','email'] 
  
  
class ProfileUpdateForm(ModelForm):
  class Meta:
    model = Profile 
    fields = ['image','bio'] 
    