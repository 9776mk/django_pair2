from django.urls import path
from . import views


app_name = "movies"

urlpatterns = [
    path("", views.main, name="main"),
    path("index/", views.index, name="index"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("create/", views.create, name="create"),
    path("<int:pk>/update/", views.update, name="update"),
]
