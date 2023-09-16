from django.urls import path 
from . import views 
from django.conf import settings
from django.conf.urls.static  import static 

urlpatterns = [
  path("" , views.Home , name = "home"),
  path("login/" , views.login_User, name = "login"),
  path("register/" , views.registerUser, name = "register"),
  path("logout/" , views.logout_User, name = "logout"),
  path("create-post/" , views.createPost , name = "create-post"),
  path("update-post/<str:pk>" , views.updatePost , name = "update-post"),
  path("delete-post/<str:pk>" , views.deletePost , name = "delete-post"),
  path("post/<str:pk>" , views.post , name = "post"),
  path("profile/<str:pk>" , views.profile , name = "profile"),
  path("update-profile/<str:pk>" , views.updateProfile , name = "update-profile"),
]

if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
  