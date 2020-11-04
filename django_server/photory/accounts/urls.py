from django.urls import path
from . import views

urlpatterns = [

    path('userinfo/', views.update_userinfo), # 유저정보 nickname,profile 수정
]