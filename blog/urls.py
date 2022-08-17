from django.urls import path, include
from .views import *


app_name = 'blog'
urlpatterns = [
    path("" , index,name="index"),
    path("detail/<slug:slug>" , detail , name='detail'),
    path("contact/" , contact , name="contact"),
    path("about/", about , name="about"),
    #path("post/", post , name="post"),

]
