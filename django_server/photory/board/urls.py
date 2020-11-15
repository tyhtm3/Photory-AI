from django.urls import path
from . import views

urlpatterns = [
    path('',views.article_list),
    path('list/<int:pagenum>/', views.index),
    path('<int:article_pk>/detail/', views.article_detail),
    path('create/', views.article_create), # create
    path('<int:article_pk>/', views.article_delete_update), # 수정삭제
    path('count/', views.article_count),
    # path('comment/list/<int:travel_id>/', views.CommentList.as_view()),
	# path('comment/delete/<int:comment_id>/', views.CommentDetail.as_view()),

]