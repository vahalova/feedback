from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),

]
