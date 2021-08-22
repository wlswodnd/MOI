from django.urls import path , include
from . import views

urlpatterns = [
    path('index',views.index),
    path('information',views.information),
    path('Introduce',views.Introduce),
    #path('login',views.login),
    #path('join',views.join),
    #path('게시판',views.게시판),
    #path('상세페이지',views.상세페이지),
    #path('수정',views.수정),
    #path('글쓰기',views.글쓰기),
]