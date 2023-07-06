from django.urls import path
from . import views

urlpatterns = [
path('', views.hello),
    path('index/', views.mail),
path('send/', views.send),
]
