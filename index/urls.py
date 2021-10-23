from django.urls import path , include
from . import views

urlpatterns = [
    path('index',views.index),
    path('Introduce',views.Introduce),
    path('Seoul',views.Seoul),
    path('Jeju',views.Jeju),
    path('Busan',views.Busan),
    path('Jeonju',views.Jeonju),
    path('Gyeongju', views.Gyeongju),
    path('Daegu', views.Daegu),
    path('Gangneung', views.Gangneung),
    path('Sokcho', views.Sokcho),
    path('Cheonan', views.Cheonan),
    path('Boryeong', views.Boryeong),
    path('Gwangju', views.Gwangju),
    path('Incheon', views.Incheon),
    path('Mokpo', views.Mokpo),
    path('ChunCheon', views.ChunCheon),
    path('Wonju', views.Wonju),
    path('map', views.map),
]