from django.urls import path
from . import views

urlpatterns = [
    path('',views.storys_crud),
    
]