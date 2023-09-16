from django.shortcuts import render ,redirect ,HttpResponse 
from .models import Post ,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from .forms import CreatePostForm , UserUpdateForm , ProfileUpdateForm 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate , login , logout 

from django.contrib.auth.decorators import login_required 

# Create your views here. 
@login_required(login_url="login")
def Home(request):
  posts = Post.objects.all() 
  title = "Home"
  return render (request, 'base/home.html',{'posts':posts ,'title':title})
  
@login_required(login_url="login") 
def post(request,pk): 
 single_post = Post.objects.get(id=pk)
 title = "View-Post "
 context = { 'post': single_post ,'title':title} 
 return render (request,'base/post.html' ,context)

@login_required(login_url="login")
def createPost(request):
  title = "Create Post"
  form = CreatePostForm() 
  if request.method == "POST":
    form = CreatePostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False) 
      post.author = request.user 
      post.save()
      return redirect('home') 
  return render(request , 'base/create_post.html',{"form":form , "title":title})
  
@login_required(login_url="login")  
def updatePost(request,pk):
  post = Post.objects.get(id=pk)
  form = CreatePostForm(instance=post)
  if request.method == 'POST':
    form = CreatePostForm(request.POST,instance=post) 
    if form.is_valid():
      form.save() 
      return redirect("home") 
  return render(request,"base/create_post.html",{"form":form}) 
  
  
@login_required(login_url="login")  
def deletePost(request,pk):
  post = Post.objects.get(id=pk) 
  if request.method == "POST":
    post.delete() 
    return redirect('home') 
  return render(request,"base/delete_page.html",{"obj":post ,'title':"Delete"}) 
  
  
def login_User(request): 
  if request.user.is_authenticated:
    return redirect("home") 
    
  if request.method ==  "POST":
    username = request.POST.get('username').title()
    password = request.POST['password'] 
    try:
      user = User.objects.get(username=username) 
    except:
      messages.error(request,"User Does not Exist !") 
    user = authenticate(username=username,password=password) 
    if user is not None:
      login(request,user) 
      messages.success(request,f"{username.title()} is logged in") 
      return redirect ('home')
    else:
      messages.error(request,"Invalid Credentials.")
  page = "Login" 
  return render(request , "base/login_register.html",{"page": page
  ,'title':'Login'}) 
  
def logout_User(request):
  logout (request) 
  return redirect("home") 
  
def registerUser (request):
  form = UserCreationForm()
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    form = UserCreationForm(request.POST) 
    
    if form.is_valid():
      user = form.save(commit=False) 
      login(request,user) 
      return redirect ('home')
      messages.success(request,"Account Created Successfully.")
      return redirect('login')

  return render(request,"base/login_register.html",{"form":form
  ,"title":"Register"})

@login_required(login_url="login")
def profile(request,pk):
  user = User.objects.get(username=pk)
  posts = user.post_set.all() 
  user_profile = user.profile 
  context = {'user_profile':user_profile ,"posts":posts}
  return render (request,'base/profile.html',context) 
  
  
def updateProfile(request ,pk):
  user = User.objects.get(username=pk) 
  
  if request.user != user:
    return HttpResponse("You are not allowed here !") 
    
  u_form = UserUpdateForm(instance=request.user)
  p_form = ProfileUpdateForm(instance=request.user.profile) 
  context = {
    "u_form":u_form ,
    "p_form":p_form
  } 
  if request.method == "POST":
    u_form = UserUpdateForm(request.POST , instance = request.user)
    p_form = ProfileUpdateForm(request.POST , request.FILES
    , instance = request.user.profile) 
    
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save() 
      messages.success(request,"Account updated !") 
      return redirect("profile",pk)
  return render (request,'base/update-profile.html',context) 
