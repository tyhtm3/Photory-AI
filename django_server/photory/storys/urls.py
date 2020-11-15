from django.urls import path
from . import views

urlpatterns = [
    path('',views.storys), 
    path('books/',views.books), 
    path('init/',views.storys_init), # post
    path('bookinit/',views.book_init), # post
    path('edit/',views.storys_u), # put
    path('editable/',views.ai_receive), # put
    path('<int:story_pk>/',views.story_rd), # get delete
    path('images/<int:story_pk>/',views.images_create),
    path('images/<int:story_pk>/<int:img_num>',views.get_normImg),
    path('images/<int:image_pk>/delete/',views.images_delete),
]