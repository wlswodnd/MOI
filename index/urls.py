from django.urls import path , include
from . import views

urlpatterns = [
    path('index',views.index),
    path('Seoul',views.Seoul),
    path('Jeju',views.Jeju),
    path('Busan',views.Busan),
    path('Jeonju',views.Jeonju),
    path('Gyeongju', views.Gyeongju),
    path('Introduce',views.Introduce),
]