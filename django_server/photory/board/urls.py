from django.urls import path
from . import views

urlpatterns = [
    path('',views.article_list),
    path('<int:article_pk>/detail', views.article_detail),
    path('<int:article_pk>/create', views.article_create),
    path('<int:article_pk>/delete', views.article_delete),
    path('<int:article_pk>/update', views.article_update),

    # path('comment/list/<int:travel_id>/', views.CommentList.as_view()),
	# path('comment/delete/<int:comment_id>/', views.CommentDetail.as_view()),

]