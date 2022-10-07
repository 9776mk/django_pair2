from django.urls import path  
from . import views 


app_name = "movies"

urlpatterns = [ 
    path("", views.main, name="main"),
    path("index/", views.index, name="index"),
]